import datetime
import uuid
from decimal import Decimal
from enum import Enum
from ipaddress import IPv4Address
from typing import Annotated, Any, Dict, List, Tuple, Union

import pytest
from pydantic import BaseModel
from tests.conftest import DefaultPydanticModel, DefaultPythonModelClass

from psqlpy import ConnectionPool
from psqlpy._internal.extra_types import PyCustomType
from psqlpy.extra_types import (
    BigInt,
    Float32,
    Float64,
    Integer,
    Money,
    PyBox,
    PyCircle,
    PyJSON,
    PyJSONB,
    PyLine,
    PyLineSegment,
    PyMacAddr6,
    PyMacAddr8,
    PyPath,
    PyPoint,
    PyText,
    SmallInt,
)

pytestmark = pytest.mark.anyio
now_datetime = datetime.datetime.now()
now_datetime_with_tz = datetime.datetime(
    2024,
    4,
    13,
    17,
    3,
    46,
    142574,
    tzinfo=datetime.timezone.utc,
)
uuid_ = uuid.uuid4()


async def test_as_class(
    psql_pool: ConnectionPool,
    table_name: str,
    number_database_records: int,
) -> None:
    """Test `as_class()` method."""
    select_result = await psql_pool.execute(
        f"SELECT * FROM {table_name}",
    )

    as_pydantic = select_result.as_class(
        as_class=DefaultPydanticModel,
    )
    assert len(as_pydantic) == number_database_records

    for single_record in as_pydantic:
        assert isinstance(single_record, DefaultPydanticModel)

    as_py_class = select_result.as_class(
        as_class=DefaultPythonModelClass,
    )

    assert len(as_py_class) == number_database_records

    for single_py_record in as_py_class:
        assert isinstance(single_py_record, DefaultPythonModelClass)


@pytest.mark.parametrize(
    ["postgres_type", "py_value", "expected_deserialized"],
    (
        ("BYTEA", b"Bytes", [66, 121, 116, 101, 115]),
        ("VARCHAR", "Some String", "Some String"),
        ("TEXT", "Some String", "Some String"),
        (
            "XML",
            """<?xml version="1.0"?><book><title>Manual</title><chapter>...</chapter></book>""",
            """<book><title>Manual</title><chapter>...</chapter></book>""",
        ),
        ("BOOL", True, True),
        ("INT2", SmallInt(12), 12),
        ("INT4", Integer(121231231), 121231231),
        ("INT8", BigInt(99999999999999999), 99999999999999999),
        ("MONEY", BigInt(99999999999999999), 99999999999999999),
        ("MONEY", Money(99999999999999999), 99999999999999999),
        ("NUMERIC(5, 2)", Decimal("120.12"), Decimal("120.12")),
        ("FLOAT8", 32.12329864501953, 32.12329864501953),
        ("FLOAT4", Float32(32.12329864501953), 32.12329864501953),
        ("FLOAT8", Float64(32.12329864501953), 32.12329864501953),
        ("DATE", now_datetime.date(), now_datetime.date()),
        ("TIME", now_datetime.time(), now_datetime.time()),
        ("TIMESTAMP", now_datetime, now_datetime),
        ("TIMESTAMPTZ", now_datetime_with_tz, now_datetime_with_tz),
        ("UUID", uuid_, str(uuid_)),
        ("INET", IPv4Address("192.0.0.1"), IPv4Address("192.0.0.1")),
        (
            "JSONB",
            {
                "test": ["something", 123, "here"],
                "nested": ["JSON"],
            },
            {
                "test": ["something", 123, "here"],
                "nested": ["JSON"],
            },
        ),
        (
            "JSONB",
            PyJSONB([{"array": "json"}, {"one more": "test"}]),
            [{"array": "json"}, {"one more": "test"}],
        ),
        (
            "JSON",
            {
                "test": ["something", 123, "here"],
                "nested": ["JSON"],
            },
            {
                "test": ["something", 123, "here"],
                "nested": ["JSON"],
            },
        ),
        (
            "JSON",
            PyJSON([{"array": "json"}, {"one more": "test"}]),
            [{"array": "json"}, {"one more": "test"}],
        ),
        (
            "MACADDR",
            PyMacAddr6("08:00:2b:01:02:03"),
            "08:00:2B:01:02:03",
        ),
        (
            "MACADDR8",
            PyMacAddr8("08:00:2b:01:02:03:04:05"),
            "08:00:2B:01:02:03:04:05",
        ),
        ("POINT", PyPoint([1.5, 2]), (1.5, 2.0)),
        ("POINT", PyPoint({1.2, 2.3}), (1.2, 2.3)),
        ("POINT", PyPoint((1.7, 2.8)), (1.7, 2.8)),
        ("BOX", PyBox([3.5, 3, 9, 9]), ((9.0, 9.0), (3.5, 3.0))),
        ("BOX", PyBox({(1, 2), (9, 9)}), ((9.0, 9.0), (1.0, 2.0))),
        ("BOX", PyBox(((1.7, 2.8), (9, 9))), ((9.0, 9.0), (1.7, 2.8))),
        (
            "PATH",
            PyPath([(3.5, 3), (9, 9), (8, 8)]),
            [(3.5, 3.0), (9.0, 9.0), (8.0, 8.0)],
        ),
        (
            "PATH",
            PyPath(((1.7, 2.8), (3.3, 2.5), (9, 9), (1.7, 2.8))),
            ((1.7, 2.8), (3.3, 2.5), (9.0, 9.0), (1.7, 2.8)),
        ),
        ("LINE", PyLine([-2, 1, 2]), (-2.0, 1.0, 2.0)),
        ("LINE", PyLine([1, -2, 3]), (1.0, -2.0, 3.0)),
        ("LSEG", PyLineSegment({(1, 2), (9, 9)}), [(1.0, 2.0), (9.0, 9.0)]),
        ("LSEG", PyLineSegment(((1.7, 2.8), (9, 9))), [(1.7, 2.8), (9.0, 9.0)]),
        (
            "CIRCLE",
            PyCircle((1.7, 2.8, 3)),
            ((1.7, 2.8), 3.0),
        ),
        (
            "CIRCLE",
            PyCircle([1, 2.8, 3]),
            ((1.0, 2.8), 3.0),
        ),
        (
            "VARCHAR ARRAY",
            ["Some String", "Some String"],
            ["Some String", "Some String"],
        ),
        (
            "TEXT ARRAY",
            [PyText("Some String"), PyText("Some String")],
            ["Some String", "Some String"],
        ),
        ("BOOL ARRAY", [True, False], [True, False]),
        ("INT2 ARRAY", [SmallInt(12), SmallInt(100)], [12, 100]),
        ("INT4 ARRAY", [Integer(121231231), Integer(121231231)], [121231231, 121231231]),
        (
            "INT8 ARRAY",
            [BigInt(99999999999999999), BigInt(99999999999999999)],
            [99999999999999999, 99999999999999999],
        ),
        (
            "MONEY ARRAY",
            [Money(99999999999999999), Money(99999999999999999)],
            [99999999999999999, 99999999999999999],
        ),
        (
            "NUMERIC(5, 2) ARRAY",
            [Decimal("121.23"), Decimal("188.99")],
            [Decimal("121.23"), Decimal("188.99")],
        ),
        (
            "FLOAT8 ARRAY",
            [32.12329864501953, 32.12329864501953],
            [32.12329864501953, 32.12329864501953],
        ),
        (
            "DATE ARRAY",
            [now_datetime.date(), now_datetime.date()],
            [now_datetime.date(), now_datetime.date()],
        ),
        (
            "TIME ARRAY",
            [now_datetime.time(), now_datetime.time()],
            [now_datetime.time(), now_datetime.time()],
        ),
        ("TIMESTAMP ARRAY", [now_datetime, now_datetime], [now_datetime, now_datetime]),
        (
            "TIMESTAMPTZ ARRAY",
            [now_datetime_with_tz, now_datetime_with_tz],
            [now_datetime_with_tz, now_datetime_with_tz],
        ),
        (
            "UUID ARRAY",
            [uuid_, uuid_],
            [str(uuid_), str(uuid_)],
        ),
        (
            "INET ARRAY",
            [IPv4Address("192.0.0.1"), IPv4Address("192.0.0.1")],
            [IPv4Address("192.0.0.1"), IPv4Address("192.0.0.1")],
        ),
        (
            "JSONB ARRAY",
            [
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
            ],
            [
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
            ],
        ),
        (
            "JSONB ARRAY",
            [
                PyJSONB([{"array": "json"}, {"one more": "test"}]),
                PyJSONB([{"array": "json"}, {"one more": "test"}]),
            ],
            [
                [{"array": "json"}, {"one more": "test"}],
                [{"array": "json"}, {"one more": "test"}],
            ],
        ),
        (
            "JSON ARRAY",
            [
                PyJSON(
                    {
                        "test": ["something", 123, "here"],
                        "nested": ["JSON"],
                    },
                ),
                PyJSON(
                    {
                        "test": ["something", 123, "here"],
                        "nested": ["JSON"],
                    },
                ),
            ],
            [
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
            ],
        ),
        (
            "JSON ARRAY",
            [
                PyJSON([{"array": "json"}, {"one more": "test"}]),
                PyJSON([{"array": "json"}, {"one more": "test"}]),
            ],
            [
                [{"array": "json"}, {"one more": "test"}],
                [{"array": "json"}, {"one more": "test"}],
            ],
        ),
        (
            "POINT ARRAY",
            [
                PyPoint([1.5, 2]),
                PyPoint([2, 3]),
            ],
            [
                (1.5, 2.0),
                (2.0, 3.0),
            ],
        ),
        (
            "BOX ARRAY",
            [
                PyBox([3.5, 3, 9, 9]),
                PyBox([8.5, 8, 9, 9]),
            ],
            [
                ((9.0, 9.0), (3.5, 3.0)),
                ((9.0, 9.0), (8.5, 8.0)),
            ],
        ),
        (
            "PATH ARRAY",
            [
                PyPath([(3.5, 3), (9, 9), (8, 8)]),
                PyPath([(3.5, 3), (6, 6), (3.5, 3)]),
            ],
            [
                [(3.5, 3.0), (9.0, 9.0), (8.0, 8.0)],
                ((3.5, 3.0), (6.0, 6.0), (3.5, 3.0)),
            ],
        ),
        (
            "LINE ARRAY",
            [
                PyLine([-2, 1, 2]),
                PyLine([1, -2, 3]),
            ],
            [
                (-2.0, 1.0, 2.0),
                (1.0, -2.0, 3.0),
            ],
        ),
        (
            "LSEG ARRAY",
            [
                PyLineSegment({(1, 2), (9, 9)}),
                PyLineSegment([(5.6, 3.1), (4, 5)]),
            ],
            [
                [(1.0, 2.0), (9.0, 9.0)],
                [(5.6, 3.1), (4.0, 5.0)],
            ],
        ),
        (
            "CIRCLE ARRAY",
            [
                PyCircle([1.7, 2.8, 3]),
                PyCircle([5, 1.8, 10]),
            ],
            [
                ((1.7, 2.8), 3.0),
                ((5.0, 1.8), 10.0),
            ],
        ),
    ),
)
async def test_deserialization_simple_into_python(
    psql_pool: ConnectionPool,
    postgres_type: str,
    py_value: Any,
    expected_deserialized: Any,
) -> None:
    """Test how types can cast from Python and to Python."""
    await psql_pool.execute("DROP TABLE IF EXISTS for_test")
    create_table_query = f"""
    CREATE TABLE for_test (test_field {postgres_type})
    """
    insert_data_query = """
    INSERT INTO for_test VALUES ($1)
    """
    await psql_pool.execute(querystring=create_table_query)
    await psql_pool.execute(
        querystring=insert_data_query,
        parameters=[py_value],
    )

    raw_result = await psql_pool.execute(
        querystring="SELECT test_field FROM for_test",
    )

    assert raw_result.result()[0]["test_field"] == expected_deserialized


async def test_deserialization_composite_into_python(
    psql_pool: ConnectionPool,
) -> None:
    """Test that it's possible to deserialize custom postgresql type."""
    await psql_pool.execute("DROP TABLE IF EXISTS for_test")
    await psql_pool.execute("DROP TYPE IF EXISTS all_types")
    await psql_pool.execute("DROP TYPE IF EXISTS inner_type")
    await psql_pool.execute("DROP TYPE IF EXISTS enum_type")
    await psql_pool.execute("CREATE TYPE enum_type AS ENUM ('sad', 'ok', 'happy')")
    await psql_pool.execute("CREATE TYPE inner_type AS (inner_value VARCHAR, some_enum enum_type)")
    create_type_query = """
    CREATE type all_types AS (
        bytea_ BYTEA,
        varchar_ VARCHAR,
        text_ TEXT,
        bool_ BOOL,
        int2_ INT2,
        int4_ INT4,
        int8_ INT8,
        float8_def_ FLOAT8,
        float4_ FLOAT4,
        float8_ FLOAT8,
        date_ DATE,
        time_ TIME,
        timestamp_ TIMESTAMP,
        timestampz_ TIMESTAMPTZ,
        uuid_ UUID,
        inet_ INET,
        jsonb_ JSONB,
        json_ JSON,
        point_ POINT,
        box_ BOX,
        path_ PATH,
        line_ LINE,
        lseg_ LSEG,
        circle_ CIRCLE,

        varchar_arr VARCHAR ARRAY,
        text_arr TEXT ARRAY,
        bool_arr BOOL ARRAY,
        int2_arr INT2 ARRAY,
        int4_arr INT4 ARRAY,
        int8_arr INT8 ARRAY,
        float8_arr FLOAT8 ARRAY,
        date_arr DATE ARRAY,
        time_arr TIME ARRAY,
        timestamp_arr TIMESTAMP ARRAY,
        timestampz_arr TIMESTAMPTZ ARRAY,
        uuid_arr UUID ARRAY,
        inet_arr INET ARRAY,
        jsonb_arr JSONB ARRAY,
        json_arr JSON ARRAY,
        test_inner_value inner_type,
        test_enum_type enum_type,
        point_arr POINT ARRAY,
        box_arr BOX ARRAY,
        path_arr PATH ARRAY,
        line_arr LINE ARRAY,
        lseg_arr LSEG ARRAY,
        circle_arr CIRCLE ARRAY
    )
    """
    create_table_query = """
    CREATE table for_test (custom_type all_types)
    """

    await psql_pool.execute(
        querystring=create_type_query,
    )
    await psql_pool.execute(
        querystring=create_table_query,
    )

    class TestEnum(Enum):
        OK = "ok"
        SAD = "sad"
        HAPPY = "happy"

    row_values = ", ".join([f"${index}" for index in range(1, 40)])
    row_values += ", ROW($40, $41), "
    row_values += ", ".join([f"${index}" for index in range(42, 49)])

    await psql_pool.execute(
        querystring=f"INSERT INTO for_test VALUES (ROW({row_values}))",
        parameters=[
            b"Bytes",
            "Some String",
            PyText("Some String"),
            True,
            SmallInt(123),
            Integer(199),
            BigInt(10001),
            32.12329864501953,
            Float32(32.12329864501953),
            Float64(32.12329864501953),
            now_datetime.date(),
            now_datetime.time(),
            now_datetime,
            now_datetime_with_tz,
            uuid_,
            IPv4Address("192.0.0.1"),
            {
                "test": ["something", 123, "here"],
                "nested": ["JSON"],
            },
            PyJSON(
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
            ),
            PyPoint({1.2, 2.3}),
            PyBox(((1.7, 2.8), (9, 9))),
            PyPath(((1.7, 2.8), (3.3, 2.5), (9, 9), (1.7, 2.8))),
            PyLine({-2, 1, 2}),
            PyLineSegment(((1.7, 2.8), (9, 9))),
            PyCircle([1.7, 2.8, 3]),
            ["Some String", "Some String"],
            [PyText("Some String"), PyText("Some String")],
            [True, False],
            [SmallInt(123), SmallInt(321)],
            [Integer(123), Integer(321)],
            [BigInt(10001), BigInt(10001)],
            [32.12329864501953, 32.12329864501953],
            [now_datetime.date(), now_datetime.date()],
            [now_datetime.time(), now_datetime.time()],
            [now_datetime, now_datetime],
            [now_datetime_with_tz, now_datetime_with_tz],
            [uuid_, uuid_],
            [IPv4Address("192.0.0.1"), IPv4Address("192.0.0.1")],
            [
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
                {
                    "test": ["something", 123, "here"],
                    "nested": ["JSON"],
                },
            ],
            [
                PyJSON(
                    {
                        "test": ["something", 123, "here"],
                        "nested": ["JSON"],
                    },
                ),
                PyJSON(
                    {
                        "test": ["something", 123, "here"],
                        "nested": ["JSON"],
                    },
                ),
            ],
            "inner type value",
            "happy",
            TestEnum.OK,
            [
                PyPoint([1.5, 2]),
                PyPoint([2, 3]),
            ],
            [
                PyBox([3.5, 3, 9, 9]),
                PyBox([8.5, 8, 9, 9]),
            ],
            [
                PyPath([(3.5, 3), (9, 9), (8, 8)]),
                PyPath([(3.5, 3), (6, 6), (3.5, 3)]),
            ],
            [
                PyLine([-2, 1, 2]),
                PyLine([5.6, 4, 5]),
            ],
            [
                PyLineSegment({(1, 2), (9, 9)}),
                PyLineSegment([(5.6, 3.1), (4, 5)]),
            ],
            [
                PyCircle([1.7, 2.8, 3]),
                PyCircle([5, 1.8, 10]),
            ],
        ],
    )

    class ValidateModelForInnerValueType(BaseModel):
        inner_value: str
        some_enum: TestEnum

    class ValidateModelForCustomType(BaseModel):
        bytea_: List[int]
        varchar_: str
        text_: str
        bool_: bool
        int2_: int
        int4_: int
        int8_: int
        float8_def_: float
        float4_: float
        float8_: float
        date_: datetime.date
        time_: datetime.time
        timestamp_: datetime.datetime
        timestampz_: datetime.datetime
        uuid_: uuid.UUID
        inet_: IPv4Address
        jsonb_: Dict[str, List[Union[str, int, List[str]]]]
        json_: Dict[str, List[Union[str, int, List[str]]]]
        point_: Tuple[float, float]
        box_: Tuple[Tuple[float, float], Tuple[float, float]]
        path_: List[Tuple[float, float]]
        line_: Annotated[list[float], 3]
        lseg_: Annotated[list[Tuple[float, float]], 2]
        circle_: Tuple[Tuple[float, float], float]

        varchar_arr: List[str]
        text_arr: List[str]
        bool_arr: List[bool]
        int2_arr: List[int]
        int4_arr: List[int]
        int8_arr: List[int]
        float8_arr: List[float]
        date_arr: List[datetime.date]
        time_arr: List[datetime.time]
        timestamp_arr: List[datetime.datetime]
        timestampz_arr: List[datetime.datetime]
        uuid_arr: List[uuid.UUID]
        inet_arr: List[IPv4Address]
        jsonb_arr: List[Dict[str, List[Union[str, int, List[str]]]]]
        json_arr: List[Dict[str, List[Union[str, int, List[str]]]]]
        point_arr: List[Tuple[float, float]]
        box_arr: List[Tuple[Tuple[float, float], Tuple[float, float]]]
        path_arr: List[list[Tuple[float, float]]]
        line_arr: List[Annotated[List[float], 3]]
        lseg_arr: List[Annotated[List[Tuple[float, float]], 2]]
        circle_arr: List[Tuple[Tuple[float, float], float]]

        test_inner_value: ValidateModelForInnerValueType
        test_enum_type: TestEnum

    class TopLevelModel(BaseModel):
        custom_type: ValidateModelForCustomType

    query_result = await psql_pool.execute(
        "SELECT custom_type FROM for_test",
    )

    model_result = query_result.as_class(
        as_class=TopLevelModel,
    )

    assert isinstance(model_result[0], TopLevelModel)


async def test_enum_type(psql_pool: ConnectionPool) -> None:
    """Test that we can decode ENUM type from PostgreSQL."""

    class TestEnum(Enum):
        OK = "ok"
        SAD = "sad"
        HAPPY = "happy"

    class TestStrEnum(str, Enum):
        OK = "ok"
        SAD = "sad"
        HAPPY = "happy"

    await psql_pool.execute("DROP TABLE IF EXISTS for_test")
    await psql_pool.execute("DROP TYPE IF EXISTS mood")
    await psql_pool.execute(
        "CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy')",
    )
    await psql_pool.execute(
        "CREATE TABLE for_test (test_mood mood, test_mood2 mood)",
    )

    await psql_pool.execute(
        querystring="INSERT INTO for_test VALUES ($1, $2)",
        parameters=[TestEnum.HAPPY, TestEnum.OK],
    )

    qs_result = await psql_pool.execute(
        "SELECT * FROM for_test",
    )
    assert qs_result.result()[0]["test_mood"] == TestEnum.HAPPY.value
    assert qs_result.result()[0]["test_mood"] != TestEnum.HAPPY
    assert qs_result.result()[0]["test_mood2"] == TestStrEnum.OK


async def test_custom_type_as_parameter(
    psql_pool: ConnectionPool,
) -> None:
    """Tests that we can use `PyCustomType`."""
    await psql_pool.execute("DROP TABLE IF EXISTS for_test")
    await psql_pool.execute(
        "CREATE TABLE for_test (nickname VARCHAR)",
    )

    await psql_pool.execute(
        querystring="INSERT INTO for_test VALUES ($1)",
        parameters=[PyCustomType(b"Some Real Nickname")],
    )

    qs_result = await psql_pool.execute(
        "SELECT * FROM for_test",
    )

    result = qs_result.result()
    assert result[0]["nickname"] == "Some Real Nickname"


async def test_custom_decoder(
    psql_pool: ConnectionPool,
) -> None:
    await psql_pool.execute("DROP TABLE IF EXISTS for_test")
    await psql_pool.execute(
        "CREATE TABLE for_test (geo_point POINT)",
    )

    await psql_pool.execute(
        "INSERT INTO for_test VALUES ('(1, 1)')",
    )

    def point_encoder(point_bytes: bytes) -> str:
        return "Just An Example"

    qs_result = await psql_pool.execute(
        "SELECT * FROM for_test",
    )
    result = qs_result.result(
        custom_decoders={
            "geo_point": point_encoder,
        },
    )

    assert result[0]["geo_point"] == "Just An Example"


async def test_row_factory_query_result(
    psql_pool: ConnectionPool,
    table_name: str,
    number_database_records: int,
) -> None:
    select_result = await psql_pool.execute(
        f"SELECT * FROM {table_name}",
    )

    def row_factory(db_result: Dict[str, Any]) -> List[str]:
        return list(db_result.keys())

    as_row_factory = select_result.row_factory(
        row_factory=row_factory,
    )
    assert len(as_row_factory) == number_database_records

    assert isinstance(as_row_factory[0], list)


async def test_row_factory_single_query_result(
    psql_pool: ConnectionPool,
    table_name: str,
) -> None:
    connection = await psql_pool.connection()
    select_result = await connection.fetch_row(
        f"SELECT * FROM {table_name} LIMIT 1",
    )

    def row_factory(db_result: Dict[str, Any]) -> List[str]:
        return list(db_result.keys())

    as_row_factory = select_result.row_factory(
        row_factory=row_factory,
    )
    expected_number_of_elements_in_result = 2
    assert len(as_row_factory) == expected_number_of_elements_in_result

    assert isinstance(as_row_factory, list)

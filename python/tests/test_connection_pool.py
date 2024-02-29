import pytest

from psqlpy import Connection, PSQLPool, QueryResult


@pytest.mark.anyio
async def test_pool_execute(
    psql_pool: PSQLPool,
    table_name: str,
    number_database_records: int,
) -> None:
    """Test that PSQLPool can execute queries."""
    select_result = await psql_pool.execute(
        f"SELECT * FROM {table_name}",
    )

    assert type(select_result) == QueryResult

    inner_result = select_result.result()
    assert isinstance(inner_result, list)
    assert len(inner_result) == number_database_records


@pytest.mark.anyio
async def test_pool_connection(
    psql_pool: PSQLPool,
) -> None:
    """Test that PSQLPool can return single connection from the pool."""
    connection = await psql_pool.connection()
    assert isinstance(connection, Connection)
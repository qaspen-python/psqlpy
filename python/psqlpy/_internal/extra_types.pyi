from typing import Any, Sequence, Union

from typing_extensions import Self

class SmallInt:
    """Represent SmallInt in PostgreSQL and `i16` in Rust."""

    def __init__(self: Self, inner_value: int) -> None:
        """Create new instance of class.

        ### Parameters:
        - `inner_value`: int object.
        """

class Integer:
    """Represent Integer in PostgreSQL and `i32` in Rust."""

    def __init__(self: Self, inner_value: int) -> None:
        """Create new instance of class.

        ### Parameters:
        - `inner_value`: int object.
        """

class BigInt:
    """Represent BigInt in PostgreSQL and `i64` in Rust."""

    def __init__(self: Self, inner_value: int) -> None:
        """Create new instance of class.

        ### Parameters:
        - `inner_value`: int object.
        """

class PyUUID:
    """Represent UUID in PostgreSQL and Uuid in Rust."""

    def __init__(self: Self, inner_value: str) -> None:
        """Create new instance of class.

        You need to pass uuid as a str.

        ### Parameters:
        - `inner_value`: str object.
        """

class PyVarChar:
    """Represent VarChar in PostgreSQL and String in Rust."""

    def __init__(self: Self, inner_value: str) -> None:
        """Create new instance of class.

        You need to pass uuid as a str.

        ### Parameters:
        - `inner_value`: str object.
        """

class PyText:
    """Represent TEXT in PostgreSQL and String ins Rust."""

    def __init__(self: Self, inner_value: str) -> None:
        """Create new instance of class.

        You need to pass uuid as a str.

        ### Parameters:
        - `inner_value`: str object.
        """

class PyJSONB:
    """Represent JSONB field in PostgreSQL and Value in Rust."""

    def __init__(
        self: Self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        """Create new instance of PyJSON.B.

        It accepts structure that can be used in JSON/JSONB fields.

        ### Parameters:
        - `value`: value for the JSONB field.
        """

class PyJSON:
    """Represent JSON field in PostgreSQL and Value in Rust."""

    def __init__(
        self: Self,
        value: Union[
            dict[str, Any],
            list[dict[str, Any]],
        ],
    ) -> None:
        """Create new instance of PyJSON.

        It accepts structure that can be used in JSON/JSONB fields.

        ### Parameters:
        - `value`: value for the JSONB field.
        """

class PyMacAddr6:
    """Represents MACADDR in PostgreSQL."""

    def __init__(self, value: str) -> None:
        """Construct new MacAddr.

        ### Parameters:
        - `value`: value for MACADDR field.
        """

class PyMacAddr8:
    """Represents MACADDR8 in PostgreSQL."""

    def __init__(self, value: str) -> None:
        """Construct new MacAddr8.

        ### Parameters:
        - `value`: value for MACADDR8 field.
        """

class PyPoint:
    """Represent point field in PostgreSQL and Point in Rust."""

    def __init__(
        self: Self,
        value: Sequence[float],
    ) -> None:
        """Create new instance of PyPoint.

        It accepts any sequence of two float numbers.

        ### Parameters:
        - `value`: sequence of two float numbers.
        """

class PyBox:
    """Represent box field in PostgreSQL and Rect in Rust."""

    def __init__(
        self: Self,
        value: Union[
            Sequence[Sequence[float]],
            Sequence[float],
        ],
    ) -> None:
        """Create new instance of PyBox.

        You need to pass any of this structures:
        - sequence of two sequences, each with pair of float numbers
        - sequence of two pairs of float

        ### Parameters:
        - `value`: any valid sequence with two pairs of float numbers.
        """

class PyPath:
    """Represent path field in PostgreSQL and LineString in Rust."""

    def __init__(
        self: Self,
        value: Union[
            Sequence[Sequence[float]],
            Sequence[float],
        ],
    ) -> None:
        """Create new instance of PyPath.

        You need to pass any of this structures:
        - sequence of sequences, each with pair of float numbers
        - sequence with pairs of float numbers

        ### Parameters:
        - `value`: any valid structure with float numbers.
        """

class PyLine:
    """Represent line field in PostgreSQL and Line in Rust."""

    def __init__(
        self: Self,
        value: Union[
            Sequence[Sequence[float]],
            Sequence[float],
        ],
    ) -> None:
        """Create new instance of PyLine.

        You need to pass any of this structures:
        - sequence of three float numbers
        - sequence of two sequences, each with pair of float numbers
        - sequence with two pairs of float numbers

        ### Parameters:
        - `value`: any valid structure with float numbers.
        """

class PyLineSegment:
    """Represent lseg field in PostgreSQL and Line in Rust."""

    def __init__(
        self: Self,
        value: Union[
            Sequence[Sequence[float]],
            Sequence[float],
        ],
    ) -> None:
        """Create new instance of PyLineSegment.

        You need to pass any of this structures:
        - sequence of two sequences, each with pair of float numbers
        - sequence with two pairs of float numbers

        ### Parameters:
        - `value`: any valid structure with float numbers.
        """

class PyPolygon:
    """Represent polygon field in PostgreSQL and Polygon in Rust."""

    def __init__(
        self: Self,
        value: Union[
            Sequence[Sequence[float]],
            Sequence[float],
        ],
    ) -> None:
        """Create new instance of PyPolygon.

        You need to pass any of this structures:
        - sequence of sequences, each with pair of float numbers
        - sequence with pairs of float numbers

        ### Parameters:
        - `value`: any valid structure with float numbers.
        """

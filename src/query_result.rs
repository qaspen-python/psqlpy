use std::collections::HashMap;

use pyo3::{prelude::*, pyclass, pymethods, types::PyDict, Py, PyAny, Python, ToPyObject};
use tokio_postgres::Row;

use crate::{exceptions::rust_errors::RustPSQLDriverPyResult, value_converter::postgres_to_py};

/// Convert postgres `Row` into Python Dict.
///
/// # Errors
///
/// May return Err Result if can not convert
/// postgres type to python or set new key-value pair
/// in python dict.
fn row_to_dict<'a>(
    py: Python<'a>,
    postgres_row: &'a Row,
    custom_types: &Option<HashMap<String, Py<PyAny>>>,
) -> RustPSQLDriverPyResult<pyo3::Bound<'a, PyDict>> {
    let python_dict = PyDict::new_bound(py);
    for (column_idx, column) in postgres_row.columns().iter().enumerate() {
        let python_type = postgres_to_py(py, postgres_row, column, column_idx, custom_types)?;
        python_dict.set_item(column.name().to_object(py), python_type)?;
    }
    Ok(python_dict)
}

#[pyclass(name = "QueryResult")]
#[allow(clippy::module_name_repetitions)]
pub struct PSQLDriverPyQueryResult {
    inner: Vec<Row>,
}

impl PSQLDriverPyQueryResult {
    #[must_use]
    pub fn new(database_result: Vec<Row>) -> Self {
        PSQLDriverPyQueryResult {
            inner: database_result,
        }
    }

    #[must_use]
    pub fn is_empty(&self) -> bool {
        self.inner.is_empty()
    }
}

#[pymethods]
impl PSQLDriverPyQueryResult {
    /// Return result as a Python list of dicts.
    ///
    /// It's a common variant how to return a result for the future
    /// processing.
    ///
    /// # Errors
    ///
    /// May return Err Result if can not convert
    /// postgres type to python or set new key-value pair
    /// in python dict.
    pub fn result(
        &self,
        py: Python<'_>,
        custom_types: Option<HashMap<String, Py<PyAny>>>,
    ) -> RustPSQLDriverPyResult<Py<PyAny>> {
        let mut result: Vec<pyo3::Bound<'_, PyDict>> = vec![];
        for row in &self.inner {
            result.push(row_to_dict(py, row, &custom_types)?);
        }
        Ok(result.to_object(py))
    }

    /// Convert result from database to any class passed from Python.
    ///
    /// # Errors
    ///
    /// May return Err Result if can not convert
    /// postgres type to python or create new Python class.
    #[allow(clippy::needless_pass_by_value)]
    pub fn as_class<'a>(
        &'a self,
        py: Python<'a>,
        as_class: Py<PyAny>,
    ) -> RustPSQLDriverPyResult<Py<PyAny>> {
        let mut res: Vec<Py<PyAny>> = vec![];
        for row in &self.inner {
            let pydict: pyo3::Bound<'_, PyDict> = row_to_dict(py, row, &None)?;
            let convert_class_inst = as_class.call_bound(py, (), Some(&pydict))?;
            res.push(convert_class_inst);
        }

        Ok(res.to_object(py))
    }
}

#[pyclass(name = "SingleQueryResult")]
#[allow(clippy::module_name_repetitions)]
pub struct PSQLDriverSinglePyQueryResult {
    inner: Row,
}

impl PSQLDriverSinglePyQueryResult {
    #[must_use]
    pub fn new(database_row: Row) -> Self {
        PSQLDriverSinglePyQueryResult {
            inner: database_row,
        }
    }

    pub fn get_inner(self) -> Row {
        self.inner
    }
}

#[pymethods]
impl PSQLDriverSinglePyQueryResult {
    /// Return result as a Python dict.
    ///
    /// This result is used to return single row.
    ///
    /// # Errors
    ///
    /// May return Err Result if can not convert
    /// postgres type to python, can not set new key-value pair
    /// in python dict or there are no result.
    pub fn result(&self, py: Python<'_>) -> RustPSQLDriverPyResult<Py<PyAny>> {
        Ok(row_to_dict(py, &self.inner, &None)?.to_object(py))
    }

    /// Convert result from database to any class passed from Python.
    ///
    /// # Errors
    ///
    /// May return Err Result if can not convert
    /// postgres type to python, can not create new Python class
    /// or there are no results.
    #[allow(clippy::needless_pass_by_value)]
    pub fn as_class<'a>(
        &'a self,
        py: Python<'a>,
        as_class: Py<PyAny>,
    ) -> RustPSQLDriverPyResult<Py<PyAny>> {
        let pydict: pyo3::Bound<'_, PyDict> = row_to_dict(py, &self.inner, &None)?;
        Ok(as_class.call_bound(py, (), Some(&pydict))?)
    }
}

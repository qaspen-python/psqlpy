import comp from "/Users/aleksandrkiselev/Projects/qaspen-python/psqlpy/docs/.vuepress/.temp/pages/usage/types/supported_types.html.vue"
const data = JSON.parse("{\"path\":\"/usage/types/supported_types.html\",\"title\":\"Supported Types\",\"lang\":\"en-US\",\"frontmatter\":{\"title\":\"Supported Types\",\"description\":\"Simple Type Here you can find all types supported by PSQLPy. If PSQLPy isn't -, you can go to the Extra Types for more information. Important DECIMAL PostgreSQL type isn't suppo...\",\"head\":[[\"meta\",{\"property\":\"og:url\",\"content\":\"https://qaspen-python.github.io/psqlpy-docs/usage/types/supported_types.html\"}],[\"meta\",{\"property\":\"og:site_name\",\"content\":\"PSQLPy\"}],[\"meta\",{\"property\":\"og:title\",\"content\":\"Supported Types\"}],[\"meta\",{\"property\":\"og:description\",\"content\":\"Simple Type Here you can find all types supported by PSQLPy. If PSQLPy isn't -, you can go to the Extra Types for more information. Important DECIMAL PostgreSQL type isn't suppo...\"}],[\"meta\",{\"property\":\"og:type\",\"content\":\"article\"}],[\"meta\",{\"property\":\"og:locale\",\"content\":\"en-US\"}],[\"script\",{\"type\":\"application/ld+json\"},\"{\\\"@context\\\":\\\"https://schema.org\\\",\\\"@type\\\":\\\"Article\\\",\\\"headline\\\":\\\"Supported Types\\\",\\\"image\\\":[\\\"\\\"],\\\"dateModified\\\":null,\\\"author\\\":[]}\"]]},\"headers\":[{\"level\":2,\"title\":\"Simple Type\",\"slug\":\"simple-type\",\"link\":\"#simple-type\",\"children\":[]},{\"level\":2,\"title\":\"Array Type\",\"slug\":\"array-type\",\"link\":\"#array-type\",\"children\":[]},{\"level\":2,\"title\":\"Composite Type\",\"slug\":\"composite-type\",\"link\":\"#composite-type\",\"children\":[]},{\"level\":2,\"title\":\"Enum Type\",\"slug\":\"enum-type\",\"link\":\"#enum-type\",\"children\":[]}],\"filePathRelative\":\"usage/types/supported_types.md\",\"autoDesc\":true,\"excerpt\":\"<h2>Simple Type</h2>\\n<p>Here you can find all types supported by <code>PSQLPy</code>. If PSQLPy isn't <code>-</code>, you can go to the <code>Extra Types</code> for more information.</p>\\n<table>\\n<thead>\\n<tr>\\n<th style=\\\"text-align:center\\\">Python type</th>\\n<th style=\\\"text-align:center\\\">PSQLPy extra type</th>\\n<th style=\\\"text-align:center\\\">PostgreSQL Type</th>\\n</tr>\\n</thead>\\n<tbody>\\n<tr>\\n<td style=\\\"text-align:center\\\">None</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">NULL</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">bool</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">BOOL</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">bytes</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">BYTEA</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">str</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">VARCHAR</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">str</td>\\n<td style=\\\"text-align:center\\\">PyVarChar</td>\\n<td style=\\\"text-align:center\\\">VARCHAR</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">str</td>\\n<td style=\\\"text-align:center\\\">PyText</td>\\n<td style=\\\"text-align:center\\\">TEXT</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">str</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">XML</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">int</td>\\n<td style=\\\"text-align:center\\\">SmallInt</td>\\n<td style=\\\"text-align:center\\\">SMALLINT</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">int</td>\\n<td style=\\\"text-align:center\\\">INTEGER</td>\\n<td style=\\\"text-align:center\\\">INTEGER</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">int</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">INTEGER</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">int</td>\\n<td style=\\\"text-align:center\\\">BIGINT</td>\\n<td style=\\\"text-align:center\\\">BIGINT</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">float</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">FLOAT4</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">float</td>\\n<td style=\\\"text-align:center\\\">Float32</td>\\n<td style=\\\"text-align:center\\\">FLOAT4</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">float</td>\\n<td style=\\\"text-align:center\\\">Float64</td>\\n<td style=\\\"text-align:center\\\">FLOAT8</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">datetime.date</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">DATE</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">datetime.time</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">TIME</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">datetime.datetime</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">TIMESTAMP</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">datetime.datetime</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">TIMESTAMPTZ</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">UUID</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">UUID</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">dict</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">JSONB</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">dict</td>\\n<td style=\\\"text-align:center\\\">PyJSONB</td>\\n<td style=\\\"text-align:center\\\">JSONB</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">dict</td>\\n<td style=\\\"text-align:center\\\">PyJSON</td>\\n<td style=\\\"text-align:center\\\">JSON</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">Mac Address 6</td>\\n<td style=\\\"text-align:center\\\">PyMacAddr6</td>\\n<td style=\\\"text-align:center\\\">MacAddr</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">Mac Address 8</td>\\n<td style=\\\"text-align:center\\\">PyMacAddr8</td>\\n<td style=\\\"text-align:center\\\">MacAddr</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">IPv4Address</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">INET</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">IPv6Address</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">INET</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">decimal.Decimal</td>\\n<td style=\\\"text-align:center\\\">-</td>\\n<td style=\\\"text-align:center\\\">NUMERIC</td>\\n</tr>\\n<tr>\\n<td style=\\\"text-align:center\\\">int/str</td>\\n<td style=\\\"text-align:center\\\">Money</td>\\n<td style=\\\"text-align:center\\\">MONEY</td>\\n</tr>\\n</tbody>\\n</table>\"}")
export { comp, data }

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
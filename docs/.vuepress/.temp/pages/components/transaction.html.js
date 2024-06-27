import comp from "/Users/aleksandrkiselev/Projects/qaspen-python/psqlpy/docs/.vuepress/.temp/pages/components/transaction.html.vue"
const data = JSON.parse("{\"path\":\"/components/transaction.html\",\"title\":\"Transaction\",\"lang\":\"en-US\",\"frontmatter\":{\"title\":\"Transaction\",\"description\":\"Transaction object represents PostgreSQL transaction. There are two ways of how we can work with transactions on PSQLPy side. Transaction parameters isolation_level: level of is...\",\"head\":[[\"meta\",{\"property\":\"og:url\",\"content\":\"https://psqlpy.github.io/components/transaction.html\"}],[\"meta\",{\"property\":\"og:site_name\",\"content\":\"PSQLPy\"}],[\"meta\",{\"property\":\"og:title\",\"content\":\"Transaction\"}],[\"meta\",{\"property\":\"og:description\",\"content\":\"Transaction object represents PostgreSQL transaction. There are two ways of how we can work with transactions on PSQLPy side. Transaction parameters isolation_level: level of is...\"}],[\"meta\",{\"property\":\"og:type\",\"content\":\"article\"}],[\"meta\",{\"property\":\"og:locale\",\"content\":\"en-US\"}],[\"script\",{\"type\":\"application/ld+json\"},\"{\\\"@context\\\":\\\"https://schema.org\\\",\\\"@type\\\":\\\"Article\\\",\\\"headline\\\":\\\"Transaction\\\",\\\"image\\\":[\\\"\\\"],\\\"dateModified\\\":null,\\\"author\\\":[]}\"]]},\"headers\":[{\"level\":3,\"title\":\"Transaction parameters\",\"slug\":\"transaction-parameters\",\"link\":\"#transaction-parameters\",\"children\":[]},{\"level\":3,\"title\":\"Control transaction fully on your own.\",\"slug\":\"control-transaction-fully-on-your-own\",\"link\":\"#control-transaction-fully-on-your-own\",\"children\":[]},{\"level\":3,\"title\":\"Control transaction with async context manager.\",\"slug\":\"control-transaction-with-async-context-manager\",\"link\":\"#control-transaction-with-async-context-manager\",\"children\":[]},{\"level\":2,\"title\":\"Transaction methods\",\"slug\":\"transaction-methods\",\"link\":\"#transaction-methods\",\"children\":[{\"level\":3,\"title\":\"Begin\",\"slug\":\"begin\",\"link\":\"#begin\",\"children\":[]},{\"level\":3,\"title\":\"Commit\",\"slug\":\"commit\",\"link\":\"#commit\",\"children\":[]},{\"level\":3,\"title\":\"Execute\",\"slug\":\"execute\",\"link\":\"#execute\",\"children\":[]},{\"level\":3,\"title\":\"Fetch\",\"slug\":\"fetch\",\"link\":\"#fetch\",\"children\":[]},{\"level\":3,\"title\":\"Execute Many\",\"slug\":\"execute-many\",\"link\":\"#execute-many\",\"children\":[]},{\"level\":3,\"title\":\"Fetch Row\",\"slug\":\"fetch-row\",\"link\":\"#fetch-row\",\"children\":[]},{\"level\":3,\"title\":\"Fetch Val\",\"slug\":\"fetch-val\",\"link\":\"#fetch-val\",\"children\":[]},{\"level\":3,\"title\":\"Pipeline\",\"slug\":\"pipeline\",\"link\":\"#pipeline\",\"children\":[]},{\"level\":3,\"title\":\"Create Savepoint\",\"slug\":\"create-savepoint\",\"link\":\"#create-savepoint\",\"children\":[]},{\"level\":3,\"title\":\"Rollback\",\"slug\":\"rollback\",\"link\":\"#rollback\",\"children\":[]},{\"level\":3,\"title\":\"Rollback Savepoint\",\"slug\":\"rollback-savepoint\",\"link\":\"#rollback-savepoint\",\"children\":[]},{\"level\":3,\"title\":\"Release Savepoint\",\"slug\":\"release-savepoint\",\"link\":\"#release-savepoint\",\"children\":[]},{\"level\":3,\"title\":\"Cursor\",\"slug\":\"cursor\",\"link\":\"#cursor\",\"children\":[]}]}],\"filePathRelative\":\"components/transaction.md\",\"autoDesc\":true,\"excerpt\":\"<p><code>Transaction</code> object represents <code>PostgreSQL</code> transaction.<br>\\nThere are two ways of how we can work with transactions on <code>PSQLPy</code> side.</p>\\n<h3>Transaction parameters</h3>\\n<ul>\\n<li><code>isolation_level</code>: level of isolation. Default how it is in PostgreSQL.</li>\\n<li><code>read_variant</code>: configure read variant of the transaction. Default how it is in PostgreSQL.</li>\\n<li><code>deferrable</code>: configure deferrable of the transaction. Default how it is in PostgreSQL.</li>\\n</ul>\"}")
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

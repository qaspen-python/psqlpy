import comp from "/Users/aleksandrkiselev/Projects/qaspen-python/psqlpy/docs/.vuepress/.temp/pages/usage/frameworks/robyn.html.vue"
const data = JSON.parse("{\"path\":\"/usage/frameworks/robyn.html\",\"title\":\"Robyn\",\"lang\":\"en-US\",\"frontmatter\":{\"title\":\"Robyn\",\"description\":\"There is the default example for Robyn framework. We strongly recommend to use the following example as a standard way to use PSQLPy with Robyn framework. Complete example\",\"head\":[[\"meta\",{\"property\":\"og:url\",\"content\":\"https://psqlpy.github.io/usage/frameworks/robyn.html\"}],[\"meta\",{\"property\":\"og:site_name\",\"content\":\"PSQLPy\"}],[\"meta\",{\"property\":\"og:title\",\"content\":\"Robyn\"}],[\"meta\",{\"property\":\"og:description\",\"content\":\"There is the default example for Robyn framework. We strongly recommend to use the following example as a standard way to use PSQLPy with Robyn framework. Complete example\"}],[\"meta\",{\"property\":\"og:type\",\"content\":\"article\"}],[\"meta\",{\"property\":\"og:locale\",\"content\":\"en-US\"}],[\"script\",{\"type\":\"application/ld+json\"},\"{\\\"@context\\\":\\\"https://schema.org\\\",\\\"@type\\\":\\\"Article\\\",\\\"headline\\\":\\\"Robyn\\\",\\\"image\\\":[\\\"\\\"],\\\"dateModified\\\":null,\\\"author\\\":[]}\"]]},\"headers\":[{\"level\":2,\"title\":\"Complete example\",\"slug\":\"complete-example\",\"link\":\"#complete-example\",\"children\":[]}],\"filePathRelative\":\"usage/frameworks/robyn.md\",\"autoDesc\":true,\"excerpt\":\"<p>There is the default example for <code>Robyn</code> framework.</p>\\n<p>We strongly recommend to use the following example as a standard way to use <code>PSQLPy</code> with <code>Robyn</code> framework.</p>\\n<h2>Complete example</h2>\\n<div class=\\\"language-python\\\" data-ext=\\\"py\\\" data-title=\\\"py\\\"><pre class=\\\"language-python\\\"><code><span class=\\\"token comment\\\"># Start example</span>\\n<span class=\\\"token keyword\\\">from</span> __future__ <span class=\\\"token keyword\\\">import</span> annotations\\n\\n<span class=\\\"token keyword\\\">import</span> asyncio\\n<span class=\\\"token keyword\\\">from</span> typing <span class=\\\"token keyword\\\">import</span> Any\\n\\n<span class=\\\"token keyword\\\">from</span> psqlpy <span class=\\\"token keyword\\\">import</span> ConnectionPool\\n<span class=\\\"token keyword\\\">from</span> robyn <span class=\\\"token keyword\\\">import</span> Request<span class=\\\"token punctuation\\\">,</span> Robyn\\n\\ndb_pool <span class=\\\"token operator\\\">=</span> ConnectionPool<span class=\\\"token punctuation\\\">(</span>\\n    dsn<span class=\\\"token operator\\\">=</span><span class=\\\"token string\\\">\\\"postgres://postgres:postgres@localhost:5432/postgres\\\"</span><span class=\\\"token punctuation\\\">,</span>\\n    max_db_pool_size<span class=\\\"token operator\\\">=</span><span class=\\\"token number\\\">10</span><span class=\\\"token punctuation\\\">,</span>\\n<span class=\\\"token punctuation\\\">)</span>\\n\\napp <span class=\\\"token operator\\\">=</span> Robyn<span class=\\\"token punctuation\\\">(</span>__file__<span class=\\\"token punctuation\\\">)</span>\\n\\n\\n<span class=\\\"token decorator annotation punctuation\\\">@app<span class=\\\"token punctuation\\\">.</span>get</span><span class=\\\"token punctuation\\\">(</span><span class=\\\"token string\\\">\\\"/\\\"</span><span class=\\\"token punctuation\\\">)</span>\\n<span class=\\\"token keyword\\\">async</span> <span class=\\\"token keyword\\\">def</span> <span class=\\\"token function\\\">pg_pool_example</span><span class=\\\"token punctuation\\\">(</span>request<span class=\\\"token punctuation\\\">:</span> Request<span class=\\\"token punctuation\\\">)</span> <span class=\\\"token operator\\\">-</span><span class=\\\"token operator\\\">&gt;</span> <span class=\\\"token builtin\\\">list</span><span class=\\\"token punctuation\\\">[</span><span class=\\\"token builtin\\\">dict</span><span class=\\\"token punctuation\\\">[</span>Any<span class=\\\"token punctuation\\\">,</span> Any<span class=\\\"token punctuation\\\">]</span><span class=\\\"token punctuation\\\">]</span><span class=\\\"token punctuation\\\">:</span>\\n    connection <span class=\\\"token operator\\\">=</span> <span class=\\\"token keyword\\\">await</span> db_pool<span class=\\\"token punctuation\\\">.</span>connection<span class=\\\"token punctuation\\\">(</span><span class=\\\"token punctuation\\\">)</span>\\n    query_result <span class=\\\"token operator\\\">=</span> <span class=\\\"token keyword\\\">await</span> connection<span class=\\\"token punctuation\\\">.</span>execute<span class=\\\"token punctuation\\\">(</span>\\n        <span class=\\\"token string\\\">\\\"SELECT * FROM users\\\"</span><span class=\\\"token punctuation\\\">,</span>\\n    <span class=\\\"token punctuation\\\">)</span>\\n    <span class=\\\"token keyword\\\">return</span> query_result<span class=\\\"token punctuation\\\">.</span>result<span class=\\\"token punctuation\\\">(</span><span class=\\\"token punctuation\\\">)</span>\\n\\n\\n<span class=\\\"token keyword\\\">async</span> <span class=\\\"token keyword\\\">def</span> <span class=\\\"token function\\\">main</span><span class=\\\"token punctuation\\\">(</span><span class=\\\"token punctuation\\\">)</span> <span class=\\\"token operator\\\">-</span><span class=\\\"token operator\\\">&gt;</span> <span class=\\\"token boolean\\\">None</span><span class=\\\"token punctuation\\\">:</span>\\n    <span class=\\\"token keyword\\\">try</span><span class=\\\"token punctuation\\\">:</span>\\n        app<span class=\\\"token punctuation\\\">.</span>start<span class=\\\"token punctuation\\\">(</span>host<span class=\\\"token operator\\\">=</span><span class=\\\"token string\\\">\\\"127.0.0.1\\\"</span><span class=\\\"token punctuation\\\">,</span> port<span class=\\\"token operator\\\">=</span><span class=\\\"token number\\\">8000</span><span class=\\\"token punctuation\\\">)</span>\\n    <span class=\\\"token keyword\\\">finally</span><span class=\\\"token punctuation\\\">:</span>\\n        db_pool<span class=\\\"token punctuation\\\">.</span>close<span class=\\\"token punctuation\\\">(</span><span class=\\\"token punctuation\\\">)</span>\\n\\n\\n<span class=\\\"token keyword\\\">if</span> __name__ <span class=\\\"token operator\\\">==</span> <span class=\\\"token string\\\">\\\"__main__\\\"</span><span class=\\\"token punctuation\\\">:</span>\\n    asyncio<span class=\\\"token punctuation\\\">.</span>run<span class=\\\"token punctuation\\\">(</span>main<span class=\\\"token punctuation\\\">(</span><span class=\\\"token punctuation\\\">)</span><span class=\\\"token punctuation\\\">)</span>\\n</code></pre></div>\"}")
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

<p>Here’s your clean “README quickstart” summary for how your MkDocs + Cloudflare Pages setup works now that everything’s running perfectly — no errors, no missing files.</p>
<p>⸻</p>
<p>🧭 Yegge Docs — Setup &amp; Deployment Guide</p>
<p>This project is a static documentation site built with MkDocs Material, styled with the custom LikeAGhost dark theme, and deployed directly to Cloudflare Pages using Wrangler.</p>
<p>⸻</p>
<p>⚙️ Directory Structure</p>
<p>yegge-docs/<br />
├── mkdocs.yml                 # main site configuration<br />
├── docs/                      # markdown source files<br />
│   ├── index.md               # homepage<br />
│   ├── about.md               # example page<br />
│   ├── ai-prompts/            # section folder<br />
│   │   ├── index.md<br />
│   │   ├── 01--prompt-one.md<br />
│   │   ├── 02--prompt-two.md<br />
│   │   └── 03--prompt-three.md<br />
│   ├── stylesheets/<br />
│   │   └── extra.css          # LikeAGhost theme CSS<br />
│   └── _assets/<br />
│       └── logo.svg           # logo used in header/favicon<br />
├── site/                      # auto-generated static site (ignored by Git)<br />
└── build_and_deploy.sh        # script to build + deploy</p>
<p>⸻</p>
<p>🧪 Development Workflow</p>
<ol>
<li>Local Preview</li>
</ol>
<p>Run a live dev server at <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>:</p>
<p>python3 -m mkdocs serve</p>
<p>MkDocs watches your docs/ and mkdocs.yml for changes, rebuilding automatically.</p>
<p>⸻</p>
<ol start="2">
<li>Folder Organization</li>
</ol>
<p>Each folder under docs/ is a section.<br />
Each .md file inside becomes a page.</p>
<p>Example:</p>
<p>docs/ai-prompts/<br />
index.md<br />
01--prompt-one.md<br />
02--prompt-two.md<br />
03--prompt-three.md</p>
<p>Because navigation.indexes is enabled in mkdocs.yml, MkDocs automatically adds those pages under the “A.I. Prompts” sidebar section — no need to list each one manually.</p>
<p>If you prefer explicit ordering, define it in mkdocs.yml:</p>
<p>nav:</p>
<ul>
<li>Home: index.md</li>
<li>A.I. Prompts:
<ul>
<li>ai-prompts/index.md</li>
<li>ai-prompts/01--prompt-one.md</li>
<li>ai-prompts/02--prompt-two.md</li>
<li>ai-prompts/03--prompt-three.md</li>
</ul>
</li>
</ul>
<p>⸻</p>
<p>🌑 LikeAGhost Theme</p>
<p>The site uses a custom dark theme layered on top of Material for MkDocs.</p>
<p>Configured in mkdocs.yml:</p>
<p>theme:<br />
name: material<br />
font:<br />
text: Inter<br />
code: JetBrains Mono<br />
features:<br />
- navigation.indexes<br />
- navigation.instant<br />
- content.code.copy<br />
- toc.follow</p>
<p>extra_css:</p>
<ul>
<li>stylesheets/extra.css</li>
</ul>
<p>The CSS file defines your ghostly glow palette, dark background, and soft link transitions.</p>
<p>⸻</p>
<p>🚀 Deployment (via Wrangler + Cloudflare Pages)</p>
<p>Build &amp; Deploy Command</p>
<p>python3 -m mkdocs build<br />
npx -y wrangler@latest pages deploy ./site --project-name yegge-docs --branch main</p>
<p>One-Command Shortcut</p>
<p>Run everything in one shot:</p>
<p>./build_and_deploy.sh</p>
<p>That script:<br />
1.	Builds MkDocs → generates site/<br />
2.	Deploys the site/ folder to Cloudflare Pages</p>
<p>Once deployed, you can access it at:</p>
<p><a href="https://yegge-docs.pages.dev">https://yegge-docs.pages.dev</a></p>
<p>(or your custom domain once you connect it in Cloudflare: e.g. docs.yegge.com)</p>
<p>⸻</p>
<p>✅ Known Working Config Highlights<br />
•	Custom logo: docs/_assets/logo.svg<br />
•	Custom CSS: docs/stylesheets/extra.css<br />
•	404s fixed: All asset paths under docs/<br />
•	No YAML errors: mkdocs.yml indentation verified<br />
•	Dark mode theme: fully applied and consistent<br />
•	Automatic sidebar: via navigation.indexes<br />
•	Wrangler auth: uses npx, no global install needed</p>
<p>⸻</p>
<p>🧩 Optional Automation</p>
<p>To auto-deploy every 15 minutes:</p>
<p>crontab -e</p>
<p>Add:</p>
<p>*/15 * * * * cd /Users/byegge/yegge-docs &amp;&amp; /bin/bash ./build_and_deploy.sh &gt;&gt; /Users/byegge/yegge-docs/build.log 2&gt;&amp;1</p>
<p>⸻</p>
<p>🕹️ Summary</p>
<p>Step	Command	Result<br />
Preview site locally	python3 -m mkdocs serve	Live dev server<br />
Build static site	python3 -m mkdocs build	Generates /site<br />
Deploy to Cloudflare	npx -y wrangler@latest pages deploy ./site --project-name yegge-docs --branch main	Pushes live site<br />
One-click full run	./build_and_deploy.sh	Build + deploy in one</p>
<p>⸻</p>
<p>Would you like me to write the README in Markdown format (ready to drop into README.md on GitHub or the repo root)? I can generate the exact file next.</p>

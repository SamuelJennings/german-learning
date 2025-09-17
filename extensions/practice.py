from urllib.parse import urlencode

from docutils import nodes
from docutils.parsers.rst import Directive

CHATGPT_BASE_URL = "https://chatgpt.com"

class PracticeDirective(Directive):
    has_content = True

    def run(self):
        self.assert_has_content()
        prompt = "\n".join(self.content).strip()
        params = urlencode({'prompt': prompt})
        full_url = f"{CHATGPT_BASE_URL}?{params}"

        html = f'<a href="{full_url}">Practice with ChatGPT</a>'
        node = nodes.raw('', html, format='html')
        return [node]

def setup(app):
    app.add_directive("practice", PracticeDirective)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

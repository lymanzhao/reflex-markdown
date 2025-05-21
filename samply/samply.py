import reflex as rx
from components.markdown import Markdown

# 示例 Markdown 文本
sample_markdown = f"""
# 标题 1
## 标题 2
### 标题 3
#### 标题 3

这是一段 **粗体文本** 和 *斜体文本*。

## 列表示例
- 项目 1
- 项目 2
- 项目 3

<thinking>思考</thinking>
<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
</ol>
------

```python
def hello_world():
    print("Hello, world!")
```
"""

class State(rx.State):
    pass    

def index():
    return rx.box(
        rx.heading("Markdown 示例 测试", size="1"),
        # rx.divider(),
        Markdown(
            content=sample_markdown,
            class_name="markdown-content"
        ),
        padding="2em",
        max_width="800px",
        margin="0 auto",
    )

app = rx.App()
app.add_page(index, route="/")

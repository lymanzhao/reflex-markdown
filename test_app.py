import reflex as rx
from components.improved_markdown import ImprovedMarkdown

class TestState(rx.State):
    """测试应用状态"""
    markdown_input: str = """# 欢迎使用 Markdown 测试器

## 功能特性
- **实时预览**: 输入内容立即渲染
- **错误处理**: 显示加载状态和错误信息
- **样式优化**: 美观的默认样式

## 代码示例
```python
def hello_world():
    print("Hello, Reflex!")
    return "欢迎使用 Reflex Markdown 组件"
```

## 列表示例
1. 第一项
2. 第二项
3. 第三项

### 无序列表
- 项目 A
- 项目 B
- 项目 C

## 表格示例
| 功能 | 状态 | 说明 |
|------|------|------|
| 标题渲染 | ✅ | 支持 H1-H6 |
| 代码高亮 | ✅ | 支持多种语言 |
| 表格 | ✅ | 支持基本表格 |

## 引用
> 这是一个引用示例
> 可以包含多行内容

## 自定义标签
<thinking>
这是一个思考标签，用于显示特殊内容
</thinking>

---

**试试修改左侧的内容，右侧会实时更新！**
"""
    
    def update_markdown(self, value: str):
        """更新markdown内容"""
        self.markdown_input = value

def test_page():
    """测试页面"""
    return rx.container(
        rx.heading("Reflex Markdown 组件测试", size="8", margin_bottom="1rem"),
        
        rx.text(
            "在左侧输入 Markdown 文本，右侧会实时显示渲染结果。",
            color="gray",
            margin_bottom="2rem"
        ),
        
        rx.grid(
            # 左侧输入区域
            rx.box(
                rx.heading("输入区域", size="4", margin_bottom="0.5rem"),
                rx.text_area(
                    value=TestState.markdown_input,
                    on_change=TestState.update_markdown,
                    placeholder="在这里输入 Markdown 文本...",
                    height="500px",
                    width="100%",
                    resize="vertical",
                    font_family="Monaco, Menlo, 'Ubuntu Mono', monospace",
                    font_size="14px",
                    line_height="1.5",
                    padding="1rem",
                    border="1px solid var(--gray-6)",
                    border_radius="8px",
                    background_color="var(--gray-1)"
                ),
                padding="1rem",
                border="1px solid var(--gray-4)",
                border_radius="8px",
                background_color="white"
            ),
            
            # 右侧预览区域
            rx.box(
                rx.heading("预览区域", size="4", margin_bottom="0.5rem"),
                rx.box(
                    ImprovedMarkdown(
                        content=TestState.markdown_input,
                        padding="1rem",
                        border="1px solid var(--gray-4)",
                        border_radius="8px",
                        background_color="white",
                        min_height="500px"
                    ),
                    width="100%"
                ),
                padding="1rem",
                border="1px solid var(--gray-4)",
                border_radius="8px",
                background_color="var(--gray-1)"
            ),
            
            columns="2",
            spacing="4",
            width="100%"
        ),
        
        # 底部说明
        rx.box(
            rx.heading("测试说明", size="4", margin_bottom="0.5rem"),
            rx.unordered_list(
                rx.list_item("修改左侧文本内容，右侧会实时更新"),
                rx.list_item("支持所有标准 Markdown 语法"),
                rx.list_item("包含错误处理和加载状态显示"),
                rx.list_item("自定义 <thinking> 标签会特殊显示"),
                rx.list_item("如果遇到渲染错误，会显示错误信息")
            ),
            margin_top="2rem",
            padding="1rem",
            border="1px solid var(--blue-4)",
            border_radius="8px",
            background_color="var(--blue-1)"
        ),
        
        max_width="1200px",
        margin="0 auto",
        padding="2rem"
    )

def simple_test_page():
    """简单测试页面 - 用于调试"""
    test_content = """# 简单测试

这是一个**简单的测试**。

- 项目 1
- 项目 2

```python
print("Hello World")
```
"""
    
    return rx.container(
        rx.heading("简单 Markdown 测试", size="6", margin_bottom="1rem"),
        rx.text("这是一个简单的静态测试页面", margin_bottom="1rem"),
        ImprovedMarkdown(
            content=test_content,
            padding="1rem",
            border="1px solid #ccc",
            border_radius="8px"
        ),
        max_width="800px",
        margin="0 auto",
        padding="2rem"
    )

# 创建应用
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="medium",
        scaling="100%"
    )
)

# 添加页面
app.add_page(test_page, route="/", title="Markdown 测试器")
app.add_page(simple_test_page, route="/simple", title="简单测试")

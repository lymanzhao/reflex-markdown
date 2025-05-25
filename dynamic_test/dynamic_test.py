import reflex as rx

class DynamicState(rx.State):
    """简化的状态管理"""
    markdown_content: str = """# 动态 Markdown 测试

## 实时编辑功能
在左侧输入框中修改内容，右侧会实时更新显示。

### 支持的功能
- **粗体文本**
- *斜体文本*
- `行内代码`

### 代码块
```python
def hello_world():
    print("Hello, Reflex!")
    return "动态测试成功"
```

### 列表
1. 第一项
2. 第二项
3. 第三项

- 项目 A
- 项目 B
- 项目 C

### 表格
| 功能 | 状态 | 说明 |
|------|------|------|
| 实时编辑 | ✅ | 支持 |
| 语法高亮 | ✅ | 支持 |
| 表格渲染 | ✅ | 支持 |

### 引用
> 这是一个引用示例
> 支持多行内容

### 自定义标签
<thinking>
这是一个思考标签，用于显示特殊内容
</thinking>

---

**试试修改左侧的内容，右侧会立即更新！**
"""

def index():
    """主页面"""
    return rx.container(
        rx.heading("Reflex Markdown 动态测试", size="8", margin_bottom="1rem"),
        
        rx.text(
            "在左侧输入 Markdown 文本，右侧会实时显示渲染结果。",
            color="gray",
            margin_bottom="2rem"
        ),
        
        rx.hstack(
            # 左侧输入区域
            rx.vstack(
                rx.heading("输入区域", size="4", margin_bottom="0.5rem"),
                rx.text_area(
                    value=DynamicState.markdown_content,
                    on_change=DynamicState.set_markdown_content,
                    placeholder="在这里输入 Markdown 文本...",
                    height="600px",
                    width="100%",
                    resize="vertical",
                    font_family="Monaco, Menlo, 'Ubuntu Mono', monospace",
                    font_size="14px",
                    line_height="1.5",
                    padding="1rem",
                    border="1px solid #ccc",
                    border_radius="8px",
                    background_color="#fafafa"
                ),
                width="50%",
                spacing="2"
            ),
            
            # 右侧预览区域
            rx.vstack(
                rx.heading("预览区域", size="4", margin_bottom="0.5rem"),
                rx.box(
                    rx.text(
                        DynamicState.markdown_content,
                        white_space="pre-wrap",
                        font_family="Monaco, Menlo, 'Ubuntu Mono', monospace",
                        font_size="14px",
                        line_height="1.5"
                    ),
                    padding="1rem",
                    border="1px solid #ccc",
                    border_radius="8px",
                    background_color="white",
                    min_height="600px",
                    overflow_y="auto",
                    width="100%"
                ),
                width="50%",
                spacing="2"
            ),
            
            spacing="4",
            width="100%",
            align_items="flex-start"
        ),
        
        # 底部说明
        rx.box(
            rx.heading("使用说明", size="4", margin_bottom="0.5rem"),
            rx.unordered_list(
                rx.list_item("在左侧文本框中输入或修改 Markdown 内容"),
                rx.list_item("右侧会实时显示渲染结果"),
                rx.list_item("支持所有标准 Markdown 语法"),
                rx.list_item("包含自定义 <thinking> 标签支持"),
                rx.list_item("如果遇到错误，会在预览区域显示错误信息")
            ),
            margin_top="2rem",
            padding="1rem",
            border="1px solid #0066cc",
            border_radius="8px",
            background_color="#f0f8ff"
        ),
        
        max_width="1400px",
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

app.add_page(index, route="/", title="Markdown 动态测试")

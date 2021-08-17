class DecoratorDivBlock:
    def __init__(self, style_class="style_class"):
        self.style_class = style_class

    def __call__(self, func):
        def wrap(list_: list):
            txt_bef, txt_after = f"<div class=*{self.style_class}*>\n", "\n</div>"
            result = txt_bef + func(list_) + txt_after
            return result

        return wrap


def decorator_body(func):
    def wrap(body_txt):
        top, bottom = "<body>\n", "\n</body>"
        result = top + func(body_txt) + bottom
        return result

    return wrap


def decorator_head(title='title'):
    def decorator(func):
        def wrap(list_: list):
            title_ = "<head>\n" \
                     f"<title>*{title}*</title>\n" \
                     "</head>\n"
            result = title_ + func(list_)
            return result

        return wrap
    return decorator


def decorator_html(func):
    def wrap(list_: list):
        html_top, html_bottom = '<html>\n', '\n</html>'
        result = html_top + func(list_) + html_bottom
        return result
    return wrap


@decorator_html
@decorator_head(title='f')
@decorator_body
@DecoratorDivBlock('style_class111')
def get_names_page(names_list) -> str:
    template_head = "<h3> User names: </h3>\n"
    names_ = [f"<p> {name} </p>" for name in names_list]
    string_info = template_head + "\n".join(names_)
    # string_info = template_head
    # for i, name in enumerate(names_list):
    #     if i + 1 == len(names_list):
    #         template = f"<p> {name} </p>"
    #         string_info += template
    #     else:
    #         template = f"<p> {name} </p>\n"
    #         string_info += template

    return string_info


print(get_names_page(["Misha", "Olya", "Vitaliy", "Vita"]))

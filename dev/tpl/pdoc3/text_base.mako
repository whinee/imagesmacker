## Define mini-templates for each portion of the document.

## Top Dependencies

<%!
    import re

    # Track last used H2-H5 slugs for hierarchical slugs
    last_slugs = [""] * 5  # For H2 to H6

    # Store TOC entries (level, text, slug)
    toc_entries = []

    def slugify(text: str) -> str:
        text = text.lower().strip()  # Convert to lowercase and trim spaces
        text = re.sub(r"[^\w\s-]", "", text)  # Remove special characters
        return re.sub(r"\s+", "-", text)

    def heading(level, text, prefix='', suffix=''):
        global last_slugs

        slug = slugify(text)

        index = level - 2  # H2 -> 0, H3 -> 1, ..., H6 -> 4
        last_slugs[index] = slug  # Update slug for this level

        # Reset deeper levels when a new higher-level heading appears
        for i in range(index + 1, 5):
            last_slugs[i] = ""

        # Construct hierarchical slug
        slug_parts = [s for s in last_slugs if s]  # Ignore empty parts
        slug = "-".join(slug_parts)

        toc_entries.append((level, text, slug))  # Store TOC entry

        return f'<h{level} id="{slug}"><a href="#{slug}">{prefix}{text}{suffix}</a></h{level}>\n'

    def indent(s, spaces=4):
        new = s.replace('\n', '\n' + ' ' * spaces)
        return ' ' * spaces + new.strip()

    def submodule_list_item(submodule):
        name = submodule.name
        return f"- [{name}](./" + name.split(".")[-1] + ('/index' if submodule.is_package else '') + ".md)"

    def go_back_to_index(module, top_bar: bool = False, bottom_bar: bool = False):
        bar = "---"
        name = module.name
        name_parts = name.split(".")
        if len(name_parts) == 1:
            return ""
        dots_multiplier = 1
        if module.is_package:
            dots_multiplier = 2
        return ("\n\n" + bar if top_bar else "") + "\n\n[← Go back to `" + ".".join(name_parts[:-1]) + f"`]({"." * dots_multiplier}/index.md)\n\n" + (bar + "\n\n" if bottom_bar else "")

    def reset_toc_entries_ls():
        toc_entries = []
        toc_html = ""
%>

<%def name="return_toc_entries()">
<%
    toc_html = ""
    toc_html = '<div class="toc">\n<ul>'
    for level, text, slug in toc_entries:
        indent = "    " * (level - 2)
        toc_html += f'\n{indent}<li><a href="#{slug}">{text}</a></li>'
    reset_toc_entries_ls()

    print(toc_entries)
    
    toc_html += "\n</ul>\n</div>"

%>${toc_html}
<%
    toc_html = "reset"
%>${toc_html}
</%def>

<%def name="function(func, level=2)" buffered="True">
<%
    returns = show_type_annotations and func.return_annotation() or ''
    if returns:
        returns = ' → ' + returns
%>
${heading(level, func.name, prefix="<pre>", suffix="</pre>")}
```python
(${", ".join(func.params(annotate=show_type_annotations))})${returns}
```

${func.docstring}
</%def>

<%def name="variable(var, level=2)" buffered="True">
<%
    annotation = show_type_annotations and var.type_annotation() or ''
    if annotation:
        annotation = f"\n\n```python\n{annotation}\n```"
%>
${heading(level, var.name, prefix="<pre>", suffix="</pre>")}${annotation}

${var.docstring}
</%def>

<%def name="class_(cls, level)" buffered="True">
${heading(level, cls.name, prefix="<pre>", suffix="</pre>")}<%
annotation_ls = cls.params(annotate=show_type_annotations)
if not len(annotation_ls):
    annotation = ""
else:
    annotation = f'```python\n({", ".join(annotation_ls)})\n```'
%>
${annotation}

${cls.docstring}
<%
  class_vars = cls.class_variables(show_inherited_members, sort=sort_identifiers)
  static_methods = cls.functions(show_inherited_members, sort=sort_identifiers)
  inst_vars = cls.instance_variables(show_inherited_members, sort=sort_identifiers)
  methods = cls.methods(show_inherited_members, sort=sort_identifiers)
  mro = cls.mro()
  subclasses = cls.subclasses()
%>
% if mro:
${heading(4, 'Ancestors (in MRO)')}
% for c in mro:
- ${c.refname}
% endfor

% endif
% if subclasses:
${heading(4, 'Descendants')}
% for c in subclasses:
- ${c.refname}
% endfor

% endif
% if class_vars:
${heading(4, 'Class variables')}
% for v in class_vars:
${variable(v, 5)}
% endfor
% endif
% if static_methods:
${heading(4, 'Static methods')}
% for f in static_methods:
${function(f, 5)}

% endfor
% endif
% if inst_vars:
${heading(4, 'Instance variables')}
% for v in inst_vars:
${variable(v, 5)}

% endfor
% endif
% if methods:
${heading(4, 'Methods')}
% for m in methods:
${function(m, 5)}

% endfor
% endif
</%def>


## Start the output logic for an entire module.

<%
  toc_entries = []
  variables = module.variables(sort=sort_identifiers)
  classes = module.classes(sort=sort_identifiers)
  functions = module.functions(sort=sort_identifiers)
  submodules = module.submodules()
  heading_text = 'Namespace' if module.is_namespace else 'Module'
%>

${heading(1, heading_text + " " + module.name)}
## =${'=' * (len(module.name) + len(heading_text))}

${module.docstring.strip()}

## ${heading(2, 'Table of Contents')}
## <%block name="table"/>

${go_back_to_index(module)}
% if submodules:
${heading(2, 'Sub-modules')}
    % for m in submodules:
${submodule_list_item(m)}
    % endfor
% endif

% if variables:
${heading(2, 'Variables')}
    % for v in variables:
${variable(v, 3)}

    % endfor
% endif

% if functions:
${heading(2, 'Functions')}
    % for f in functions:
${function(f, 3)}

    % endfor
% endif

% if classes:
${heading(2, 'Classes')}
    % for c in classes:
${class_(c, 3)}

    % endfor
% endif
${go_back_to_index(module, top_bar=True)}

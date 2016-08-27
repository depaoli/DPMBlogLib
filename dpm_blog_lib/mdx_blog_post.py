#!/usr/bin/env python

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

class SetTableClass(Treeprocessor):

    def run(self, root):
        """
        Automatically called when the processor is invoked, 'root' is automatically passed
        at runtime by the Markdown core as ElementTree object representing the HTML
        document
        """
        self.set_table_class(root)
        # Some may be inclined to return the modified root element. While that would work,
        # it would cause a copy of the entire ElementTree to be generated each time the
        # Treeprocessor is run. Therefore, it is generally expected that the run method
        # would only return None or a new ElementTree object.
        # (https://pythonhosted.org/Markdown/extensions/api.html#treeprocessors)

    def set_table_class(self, element):
        for child in element:
            if child.tag == 'table':
                child.set('class', 'table table-striped table-responsive')
            self.set_table_class(child)

class SetLinkTarget(Treeprocessor):

    def run(self, root):
        """
        Automatically called when the processor is invoked, 'root' is automatically passed
        at runtime by the Markdown core as ElementTree object representing the HTML
        document
        """
        self.set_link_target(root)
        # Some may be inclined to return the modified root element. While that would work,
        # it would cause a copy of the entire ElementTree to be generated each time the
        # Treeprocessor is run. Therefore, it is generally expected that the run method
        # would only return None or a new ElementTree object.
        # (https://pythonhosted.org/Markdown/extensions/api.html#treeprocessors)

    def set_link_target(self, element):
        for child in element:
            if child.tag == 'a':
                child.set('target', '_blank')
            self.set_link_target(child)


class DPMBlogPostExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.add('dpm_blog_post_tables', SetTableClass(md), '_end')
        md.treeprocessors.add('dpm_blog_post_links', SetLinkTarget(md), '_end')

def makeExtension(*args, **kwargs):
    return DPMBlogPostExtension(*args, **kwargs)

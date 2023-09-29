from typing import Tuple
from flask import render_template
import json

class ContentProvider:

    def __init__(self, DEBUG: bool) -> None:
        self.DEBUG = DEBUG

    def _read_content(self, content: str, language: str) -> dict:
        if self.DEBUG:
            path = f"/Users/tom/projects/cv-website/static/content/{language}/{content}.json"
        else:
            path = f"/app/static/content/{language}/{content}.json"

        return self._read_json(path)


    def _read_json(self, path: str) -> dict:
        with open(path, "r") as json_file:
            return json.load(json_file)


    def _read_projects(self, language: str) -> list:

        projects = []
        projects.append(self._read_content("work_projects", language))
        projects.append(self._read_content("personal_projects", language))

        return projects

    def _read_about(self, language: str) -> Tuple[list, str]:
        about_list = []
        about_dict = self._read_content("about", language)

        for item in about_dict.values():
            about_list.append(item)

        return about_list, about_dict["heading"]


    def _read_menu(self, language: str) -> dict:
        return self._read_content("menu", language)


    def _read_headings(self, language: str) -> dict:
        return self._read_content("headings", language)


    def _read_contact_form(self, language: str) -> dict:
        return self._read_content("contact_form", language)


    def _read_footer(self, language: str) -> dict:
        return self._read_content("footer", language)


    def _read_mail_status(self, language: str) -> dict:
        return self._read_content("mail_status", language)

    
    def language_site(self, page: str, language: str, mail_result: bool) -> str:
        page=page+".html"
        projects = self._read_projects(language)
        about_list, heading = self._read_about(language)
        menu = self._read_menu(language)
        headings = self._read_headings(language)
        contact_form = self._read_contact_form(language)
        footer = self._read_footer(language)
        mail_status = self._read_mail_status(language)

        return render_template(page, menu=menu, language=language, project_lists=projects, about_heading=heading, about_p=about_list, headings=headings, contact_form=contact_form, footer=footer, mail_result=mail_result, mail_status=mail_status)

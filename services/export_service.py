import json
import csv
import yaml
import xml.etree.ElementTree as ET
from pathlib import Path

from repositories.article_repository import ArticleRepository


def export_json():
    repository = ArticleRepository()
    articles = repository.get_all_with_authors()

    output_dir = Path(__file__).resolve().parent.parent / "out"
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / "data.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(articles, file, ensure_ascii=False, indent=4)

    print(f"Данные успешно сохранены в {file_path}")

def export_csv():
    repository = ArticleRepository()
    articles = repository.get_all_with_authors()

    output_dir = Path(__file__).resolve().parent.parent / "out"
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / "data.csv"

    with open(file_path, "w", encoding="utf-8-sig", newline="") as file:
        fieldnames = [
            "article_id",
            "title",
            "content",
            "author_id",
            "author_login"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for article in articles:
            author = article["author"]

            writer.writerow({
                "article_id": article["article_id"],
                "title": article["title"],
                "content": article["content"],
                "author_id": author["user_id"] if author else "",
                "author_login": author["login"] if author else ""
            })

    print(f"Данные успешно сохранены в {file_path}")

def export_xml():
    repository = ArticleRepository()
    articles = repository.get_all_with_authors()

    output_dir = Path(__file__).resolve().parent.parent / "out"
    output_dir.mkdir(parents=True, exist_ok=True)

    root = ET.Element("articles")

    for article in articles:
        article_element = ET.SubElement(root, "article")

        ET.SubElement(
            article_element, "article_id"
        ).text = str(article["article_id"])

        ET.SubElement(
            article_element, "title"
        ).text = article["title"]

        ET.SubElement(
            article_element, "content"
        ).text = article["content"]

        author = article["author"]

        if author:
            author_element = ET.SubElement(article_element, "author")

            ET.SubElement(
                author_element, "user_id"
            ).text = str(author["user_id"])

            ET.SubElement(
                author_element, "login"
            ).text = author["login"]

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")

    file_path = output_dir / "data.xml"
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

    print(f"Данные успешно сохранены в {file_path}")


def export_yaml():
    repository = ArticleRepository()
    articles = repository.get_all_with_authors()

    output_dir = Path(__file__).resolve().parent.parent / "out"
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / "data.yaml"

    with open(file_path, "w", encoding="utf-8") as file:
        yaml.dump(
            articles,
            file,
            allow_unicode=True,
            sort_keys=False,
            indent=4
        )

    print(f"Данные успешно сохранены в {file_path}")

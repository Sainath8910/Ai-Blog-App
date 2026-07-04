from .base_exporter import BaseExporter


class MarkdownExporter(BaseExporter):

    def export(self):

        lines = []

        # ------------------------------------
        # Blog Title
        # ------------------------------------

        lines.append(f"# {self.blog.title}")
        lines.append("")
        hero = self.blog.hero or {}

        image = hero.get("image", {})

        if image:

            image_url = (
                image.get("path")
                or image.get("url")
                or image.get("image_url")
            )

            alt = image.get(
                "alt_text",
                self.blog.title,
            )

            if image_url:

                lines.append(f"![{alt}]({image_url})")
                lines.append("")

        if self.blog.description:
            lines.append(self.blog.description)
            lines.append("")

        lines.append("---")
        lines.append("")

        # ------------------------------------
        # Chapters
        # ------------------------------------

        for chapter in self.chapters:

            lines.append(f"## {chapter.title}")
            lines.append("")
            image = chapter.image or {}

            image_url = (
                image.get("path")
                or image.get("url")
                or image.get("image_url")
            )

            if image_url:

                alt = image.get(
                    "alt_text",
                    chapter.title,
                )

                lines.append(f"![{alt}]({image_url})")
                lines.append("")

            # Paragraphs

            for paragraph in chapter.paragraphs:
                lines.append(paragraph)
                lines.append("")

            # Bullet Points

            if chapter.bullet_points:

                lines.append("### Key Points")
                lines.append("")

                for point in chapter.bullet_points:
                    lines.append(f"- {point}")

                lines.append("")

            # Steps

            if chapter.numbered_steps:

                lines.append("### Steps")
                lines.append("")

                for i, step in enumerate(chapter.numbered_steps, start=1):

                    if isinstance(step, dict):

                        lines.append(
                            f"{i}. {step.get('title', '')}"
                        )

                        if step.get("description"):
                            lines.append(step["description"])

                    else:
                        lines.append(f"{i}. {step}")

                lines.append("")

            # Tips

            if chapter.tips:

                lines.append("### Tips")
                lines.append("")

                for tip in chapter.tips:
                    lines.append(f"- {tip}")

                lines.append("")

            # Warnings

            if chapter.warnings:

                lines.append("### Warnings")
                lines.append("")

                for warning in chapter.warnings:
                    lines.append(f"- {warning}")

                lines.append("")

            # Notes

            if chapter.notes:

                lines.append("### Notes")
                lines.append("")

                for note in chapter.notes:
                    lines.append(f"- {note}")

                lines.append("")

            # Quotes

            if chapter.quotes:

                lines.append("### Quotes")
                lines.append("")

                for quote in chapter.quotes:
                    lines.append(f"> {quote}")

                lines.append("")

            # Code

            if chapter.code_examples:

                for code in chapter.code_examples:

                    language = code.get("language", "")

                    lines.append(f"```{language}")

                    lines.append(
                        code.get("code", "")
                    )

                    lines.append("```")
                    lines.append("")

        # ------------------------------------
        # Takeaways
        # ------------------------------------

        if self.blog.key_takeaways:

            lines.append("---")
            lines.append("")
            lines.append("## Key Takeaways")
            lines.append("")

            for takeaway in self.blog.key_takeaways:
                lines.append(f"- {takeaway}")

            lines.append("")

        # ------------------------------------
        # FAQ
        # ------------------------------------

        if self.blog.faq:

            lines.append("## FAQ")
            lines.append("")

            for item in self.blog.faq:

                lines.append(
                    f"### {item.get('question','')}"
                )

                lines.append(
                    item.get("answer","")
                )

                lines.append("")

        # ------------------------------------
        # Resources
        # ------------------------------------

        if self.blog.resources:

            lines.append("## Resources")
            lines.append("")

            for resource in self.blog.resources:

                title = resource.get("title", "")
                url = resource.get("url", "")

                lines.append(f"- [{title}]({url})")

            lines.append("")

        # ------------------------------------
        # Conclusion
        # ------------------------------------

        if self.blog.conclusion:

            lines.append("## Conclusion")
            lines.append("")
            conclusion = self.blog.conclusion or {}

            image = conclusion.get("image", {})

            image_url = (
                image.get("path")
                or image.get("url")
                or image.get("image_url")
            )

            if image_url:

                alt = image.get(
                    "alt_text",
                    "Conclusion",
                )

                lines.append(f"![{alt}]({image_url})")
                lines.append("")

            paragraphs = self.blog.conclusion.get(
                "paragraphs",
                [],
            )

            for paragraph in paragraphs:
                lines.append(paragraph)
                lines.append("")

        return "\n".join(lines)
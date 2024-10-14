from fasthtml import common as fh
import logging

logger = logging.getLogger("html_css_basics")
logger.setLevel(logging.INFO)


hdrs = [
    fh.Meta(charset="UTF-8"),
    fh.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    fh.Meta(name="description", content="Nikhil's Web Page"),
    fh.Title("Nikhil's Web Page"),
    fh.Link(
        href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
        rel="stylesheet",
    ),
    fh.Link(
        href="https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.css",
        rel="stylesheet",
    ),
]


def create_app():
    app = fh.FastHTML(
        default_hdrs=False,
        live=True,
    )

    @app.route("/", methods=["GET"])
    def root(session):
        logger.warning("Entered Root.")
        return fh.Html(
            fh.Head(*hdrs),
            fh.Body(fh.H1("Hello, World!"), fh.P("This is a simple HTML page.")),
        )

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(f"{__name__}:create_app", host="0.0.0.0", port=3000, reload=True)

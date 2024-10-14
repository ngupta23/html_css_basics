from fasthtml import common as fh
import logging

logger = logging.getLogger("html_css_basics")
logger.setLevel(logging.INFO)


def create_app():
    app = fh.FastHTML(
        default_hdrs=False,
        live=True,
    )

    @app.route("/", methods=["GET"])
    def root(session):
        logger.warning("Entered Root.")
        return fh.Html(
            fh.Head(fh.Title("Home")),
            fh.Body(fh.H1("Hello, World!"), fh.P("This is a simple HTML page.")),
        )

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(f"{__name__}:create_app", host="0.0.0.0", port=3000, reload=True)

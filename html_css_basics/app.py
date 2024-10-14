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

    blank = (fh.Div("-------"),)

    @app.route("/", methods=["GET"])
    def root(session):
        logger.warning("Entered Root.")
        return fh.Html(
            fh.Head(*hdrs),
            fh.Body(fh.H1("Hello, World!"), fh.P("This is a simple HTML page.")),
            # https://www.geeksforgeeks.org/tailwind-css-container/
            fh.Div(
                blank,
                fh.Div("mx-auto", cls="bg-green-500 text-white mx-auto"),
                blank,
                fh.Div(
                    "mx-auto with padding on x axis only - px-2",
                    cls="bg-green-500 text-white mx-auto px-2",
                ),
                blank,
                fh.Div(
                    "mx-auto with padding on y axis only - py-2",
                    cls="bg-green-500 text-white mx-auto py-2",
                ),
                blank,
                fh.Div(
                    "mx-auto with padding on both x and y axis p-2",
                    cls="bg-green-500 text-white mx-auto p-2",
                ),
            ),
            # https://www.geeksforgeeks.org/tailwind-css-box-sizing/
            fh.Div(
                blank,
                fh.Div(
                    "box-border",
                    cls="box-border bg-green-500 text-white",
                ),
                blank,
                fh.Div(
                    "box-border m-auto m4",
                    cls="box-border bg-green-500 text-white m-auto m4",
                ),
                blank,
                fh.Div(
                    "box-border with height and width set",
                    cls="box-border bg-green-500 text-white h-28 w-32",
                ),
                blank,
                fh.Div(
                    "box-border with height, width and padding set",
                    cls="box-border bg-green-500 text-white h-36 w-48 p-4",
                ),
                blank,
                fh.Div(
                    "box-content with height, width and padding set",
                    cls="box-content bg-green-500 text-white h-36 w-48 p-4",
                ),
                blank,
                fh.Div(
                    "box-content with height, width, padding and border set",
                    cls="box-content bg-green-500 text-white h-36 w-48 p-4 border-4 border-black",
                ),
            ),
            # https://www.geeksforgeeks.org/tailwind-css-display/
            fh.Div(
                blank,
                # mx-16 moves he container 16 units right from the left margin
                # space-y-4 gives a space of 4 units between the Span elements.
                fh.Div(
                    "display=Block (placed vertically - default)",
                    # takes default width since nothing has been mentioned, height = 12
                    fh.Span("1", cls="block h-12 bg-green-500 rounded-lg"),
                    fh.Span("2", cls="block h-12 bg-green-500 rounded-lg"),
                    cls="bg-green-200 p-4 mx-16 space-y-4",
                ),
                blank,
                fh.Div(
                    "display=Inline - Block (placed horizontally)",
                    fh.Span("1", cls="inline-block w-32 h-12 bg-green-500 rounded-lg"),
                    fh.Span("2", cls="inline-block w-32 h-12 bg-green-500 rounded-lg"),
                    cls="bg-green-200 p-4 mx-16 space-y-4",
                ),
                blank,
                fh.Div(
                    # Inline takes the minimum width required to fit the content.
                    # w and h are ignored
                    "display=Inline (placed horizontally with minimal width)",
                    fh.Span("1", cls="inline w-32 h-12 bg-green-500 rounded-lg"),
                    fh.Span("2", cls="inline w-32 h-12 bg-green-500 rounded-lg"),
                    cls="bg-green-200 p-4 mx-16 space-y-4",
                ),
                blank,
                fh.Div(
                    # Flex
                    "display=Flex - occupies the entire width",
                    fh.Span("1", cls="flex-1 bg-green-500 rounded-lg"),
                    fh.Span("2", cls="flex-1 bg-green-500 rounded-lg"),
                    cls="flex bg-green-200 p-4 mx-16",
                ),
            ),
            # https://www.geeksforgeeks.org/tailwind-css-flex-direction/
            fh.Div(
                blank,
                fh.Div(
                    "display=flex-row",
                    fh.Span("1", cls="bg-green-800 w-24 h-12"),
                    fh.Span("2", cls="bg-green-400 w-24 h-12"),
                    cls="flex flex-row justify-evenly",
                ),
                blank,
                fh.Div(
                    "display=flex-col",
                    fh.Span("1", cls="bg-green-800 w-24 h-12"),
                    fh.Span("2", cls="bg-green-400 w-24 h-12"),
                    cls="flex flex-col justify-evenly",
                ),
            ),
            # https://www.geeksforgeeks.org/tailwind-css-flex-wrap/
            fh.Div(
                blank,
                fh.Div(
                    "display=flex-wrap",
                    fh.Span("1", cls="bg-green-900 w-24 h-12"),
                    fh.Span("2", cls="bg-green-800 w-24 h-12"),
                    fh.Span("3", cls="bg-green-700 w-24 h-12"),
                    fh.Span("4", cls="bg-green-600 w-24 h-12"),
                    fh.Span("5", cls="bg-green-500 w-24 h-12"),
                    fh.Span("6", cls="bg-green-400 w-24 h-12"),
                    cls="ml-24 h-28 w-96 flex flex-wrap bg-green-200 border-solid border-4 border-green-900",
                ),
                blank,
                fh.Div(
                    # compresses the content irrespective of the width you have specified
                    "display=flex-nowrap",
                    fh.Span("1", cls="bg-green-900 w-24 h-12"),
                    fh.Span("2", cls="bg-green-800 w-24 h-12"),
                    fh.Span("3", cls="bg-green-700 w-24 h-12"),
                    fh.Span("4", cls="bg-green-600 w-24 h-12"),
                    fh.Span("5", cls="bg-green-500 w-24 h-12"),
                    fh.Span("6", cls="bg-green-400 w-24 h-12"),
                    cls="ml-24 h-28 w-96 flex flex-nowrap bg-green-200 border-solid border-4 border-green-900",
                ),
            ),
            # https://www.geeksforgeeks.org/tailwind-css-flex/
            fh.Div(
                blank,
                fh.Div(
                    fh.P("This is the effect of flex-1:", cls="ml-2"),
                    fh.Div(
                        fh.Div("Geeksforgeeks", cls="bg-green-900 flex-1"),
                        fh.Div("Tailwind CSS", cls="bg-green-800 flex-1"),
                        cls="flex m-2 text-white",
                    ),
                    fh.P("This is the effect of flex-initial:", cls="ml-2"),
                    fh.Div(
                        fh.Div("Geeksforgeeks", cls="bg-green-900 flex-initial"),
                        fh.Div("Tailwind CSS", cls="bg-green-800 flex-initial"),
                        cls="flex m-2 text-white",
                    ),
                    fh.P("This is the effect of flex-auto:", cls="ml-2"),
                    fh.Div(
                        fh.Div("Geeksforgeeks", cls="bg-green-900 flex-auto"),
                        fh.Div("Tailwind CSS", cls="bg-green-800 flex-auto"),
                        cls="flex m-2 text-white",
                    ),
                    fh.P("This is the effect of flex-none:", cls="ml-2"),
                    fh.Div(
                        fh.Div("Geeksforgeeks", cls="bg-green-900 flex-none"),
                        fh.Div("Tailwind CSS", cls="bg-green-800 flex-none"),
                        cls="flex m-2 text-white",
                    ),
                    id="main",
                    cls="bg-green-200 border-4 border-green-600 w-2/3 ml-32",
                ),
            ),
            # https://www.geeksforgeeks.org/tailwind-css-flex-grow/
            fh.Div(
                blank,
                fh.Div(
                    fh.P("flex-grow-0 (only grows to the space needed):", cls="ml-2"),
                    fh.Div(
                        fh.Div("Side Part", cls="rounded bg-green-600 flex-grow h-12"),
                        fh.Div(
                            "Flex-Grow-0", cls="rounded bg-green-300 flex-grow-0 h-12"
                        ),
                        fh.Div(
                            "Side Part", cls="rounded bg-green-600 flex-grow h-12 mr-12"
                        ),
                        cls="flex border-4 border-green-600 justify-evenly space-x-2 ml-12 mr-12",
                    ),
                ),
                blank,
                fh.Div(
                    fh.P("flex-grow (grows to occupy remaining space):", cls="ml-2"),
                    fh.Div(
                        fh.Div("Side Part", cls="rounded bg-green-600 w-24 h-12"),
                        fh.Div(
                            "Flex-Grow-0", cls="rounded bg-green-300 flex-grow h-12"
                        ),
                        fh.Div("Side Part", cls="rounded bg-green-600 w-24 h-12"),
                        cls="flex border-4 border-green-600 justify-evenly space-x-2 ml-12 mr-12",
                    ),
                ),
            ),
        )

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(f"{__name__}:create_app", host="0.0.0.0", port=3000, reload=True)

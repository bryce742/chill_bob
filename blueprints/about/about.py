from flask import Blueprint, render_template, current_app

about_bp = Blueprint('about', __name__, template_folder='templates')

@about_bp.route('/')
def tab3_home():
    page_config = {
        "main_heading": "swimming upstream",             # Main heading text
        "heading_color": "blue",                               # Heading text color
        "heading_font": "Arial, sans-serif",                    # Font family for heading
        "heading_font_size": "4em",                             # Font size for heading
        "heading_font_weight": "bold",                          # Font weight for heading
        "heading_padding": "0px 0",                             # Padding around heading
        "heading_alignment": "center",                          # Text alignment for heading ('left', 'center', 'right')
        "heading_background": "rgba(255, 255, 255, 0.2)",       # Background color for heading container
        "heading_border": "1px solid white",                    # Border style for heading container
        "heading_container_padding": ".5%",                     # Padding inside heading container
        "heading_display": "inline-block",                      # Display mode (inline-block to wrap content width)
        "heading_margin": "auto" if "center" else "0",          # Center if alignment is 'center'
        "heading_bottom_padding": "20px",                       # Padding below heading

        "paragraphs": "fis cycle coded",         # Main paragraph text
        "paragraph_color": "blue",                             # Paragraph text color
        "paragraph_font": "Georgia, serif",                     # Font family for paragraph
        "paragraph_font_size": "2em",                           # Font size for paragraph
        "paragraph_font_weight": "",                            # Font weight for paragraph
        "paragraph_padding": "5px 0",                           # Padding around paragraph
        "paragraph_alignment": "center",                        # Text alignment for paragraph ('left', 'center', 'right')
        "paragraph_background": "rgba(255, 255, 255, 0.2)",     # Background color for paragraph container
        "paragraph_border": "1px solid #ddd",                   # Border style for paragraph container
        "paragraph_container_padding": "10px",                  # Padding inside paragraph container
        "paragraph_display": "inline-block",                    # Display mode (inline-block to wrap content width)
        "paragraph_margin": "auto" if "center" else "0",        # Center if alignment is 'center'
        "paragraph_bottom_padding": "20px",                     # Padding below paragraph


        "content_boxed": True,                                  # Whether the content should be inside a box
        "box_background": "transparent",                        # Background color of the box (use rgba for transparency)
        "box_border": "transparent",                            # Border style of the box
        "box_padding": "0px",                                   # Padding inside the box
        "box_margin": "0px auto",                               # Margin around the box

        "background_image": "/static/media/fis_home.jpg" # Background image URL for the page
    }
    merged_config = {**current_app.config, **page_config}
    return render_template('tab3.html', **merged_config)

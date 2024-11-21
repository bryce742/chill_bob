Config file variable flexibility and what each key's value represents

Configuration Keys:
body_class: Sets the main CSS class for the body of the page. Useful for applying global styles across all pages. (e.g., "main-body")

bootstrap_link: URL to the Bootstrap CSS file. Update this to use a different version of Bootstrap or a different CSS framework if desired.

tab1_name, tab2_name, tab3_name: Display names for each tab. These are the names shown on the navbar links for each respective tab. Changing these values will update the labels without affecting functionality.

tab1_route, tab2_route, tab3_route: URL paths for each tab. Set these to define the URL structure of each tab (e.g., setting tab1_route = "about_page" makes the route /about_page).

tg_tag: Your Telegram tag for linking to your Telegram profile from the navbar. Replace "YourTelegramTag" with your actual handle.

x_tag: Your X (formerly Twitter) handle for linking to your profile. Replace "YourXHandle" with your actual X handle.

CA: Contract address or any unique identifier for a linked resource. This can be a blockchain contract address, a product code, or any other relevant identifier.

footer_text: Text displayed in the footer of the website. Modify this to show any message or copyright information.

currentPage: Sets the default page title displayed in the browser tab and on the homepage. This can be updated to reflect the main theme or purpose of the site.






_______________________
in each blueprint py file there is a page_config dictionary that gives you control over the actual CONTENT rather than functionality of each page

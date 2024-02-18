# [FETCH & FEAST](https://fetch-and-feast-4ceb13480b0c.herokuapp.com/)
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/amiresponsive.png?raw=true" alt="Fetch & Feast AmIResonsive Image">
</div>

[Fetch & Feast](https://fetch-and-feast-4ceb13480b0c.herokuapp.com/) is an ecommerce platform tailored for dog treats, food, and toys, developed on Django. It encompasses user registration, profile management, newsletter subscriptions, and product purchases facilitated by Stripe. Additionally, it hosts blogs with commenting and liking capabilities. Users can rate products post-purchase. Frontend admin controls empower easy management of products and blogs.

## Table of Contents
1. <details open>
    <summary><a href="#ux">UX</a></summary>

    <ul>
    <li><details>
    <summary><a href="#goals">Goals</a></summary>

    - [Visitor Goals](#visitor-goals)
    - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    </details></li>

    <li><details>
    <summary><a href="#visual-design">Visual Design</a></summary>

    - [Wireframes](#wireframes)
    - [Fonts](#fonts)
    - [Colors](#colors)
    </details></li>

    <li>
    <a href="#agile-development">Agile Development</a>
    </li>

    </ul>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#page-elements">Page Elements</a></summary>

    - [All Pages](#all-pages)
    - [Homepage](#homepage)
    - [Create Post Page](#create-post-page)
    - [Post Detail Page](#post-detail-page)
    - [Profile Page](#profile-page)
    - [About Page](#about-page)
    - [Login/Register Pages](#login-and-register-pages)
    - [Confirm Delete Pages](#confirm-delete-pages)
    - [Contact Page](#contact-page)
    </details></li>

    <li>
    <a href="#features-not-yet-implemented">Features Not Yet Implemented</a>
    </li>
    </ul>
</details>

3. 
    <summary><a href="#technologies-used">Technologies Used</a></summary>

4. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <ul>
    <li><details>
    <summary><a href="#automated-testing">Automated Testing</a></summary>

    - [Validation](#validation)
    - [Python Testing](#python-testing)

    </details></li>

    <li><details>
    <summary><a href="#manual-testing">Manual Testing</a></summary>

    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
    </details></li>

    <li><details>
    <summary><a href="#bugs">Bugs</a></summary>

    - [Known Bugs](#known-bugs)
    - [Fixed Bugs](#fixed-bugs)
    </details></li>
    </ul>
</details>

5. <a href="#deployment">Deployment</a>

6. <a href="#credits-and-acknowledgements">Credits and Acknowledgements</a>

----

# UX
## Goals
### Visitor Goals

Target Audience for Fetch & Feast:

- Dog owners and enthusiasts seeking high-quality treats, food, and toys for their pets.
- Individuals looking for a convenient and reliable platform to purchase pet supplies.
- Those interested in staying updated on the latest trends and news in the pet industry.
- Pet owners seeking a community to share experiences and recommendations.

User Goals:

- Find and purchase top-quality dog treats, food, toys, and accessories.
- Connect with fellow pet owners and build a virtual pet-loving community.
- Stay informed about the latest trends, tips, and news in the pet industry.
- Easily navigate the website to discover relevant products and content.
- Customize their profiles and engage with the community through reviews, comments, and likes.

How Fetch & Feast Fulfills These Needs:

- The ecommerce platform offers a wide range of products, providing convenience and reliability for pet owners to find and purchase the best supplies for their furry companions.
- Interactive features such as blog commenting and liking foster a sense of community among pet owners, allowing them to share experiences and recommendations.
- User-friendly account management features enable customization of profiles and easy engagement with the community.
- Newsletter subscriptions keep users informed about the latest products, promotions, and trends in the pet industry.
- The platform follows standard web design conventions for easy navigation while incorporating pet-themed elements to create an engaging and user-friendly experience.

ChatGPT

### Business Goals

- Develop a dynamic and interactive ecommerce platform that offers a seamless shopping experience for pet owners, emphasizing convenience and quality.
- Drive consistent traffic by providing engaging features beyond product listings, such as interactive forums or pet care resources, fostering a thriving online community.
- Maintain a regular cadence of product updates and promotions to keep users engaged and coming back for new offerings.
- Establish Fetch & Feast as a trusted authority in the pet industry by curating and showcasing only high-quality products from reputable brands, ensuring customer satisfaction and loyalty.
- Implement strategies to highlight top-selling products, user favorites, and exclusive deals, driving sales and potentially attracting partnerships with leading pet suppliers or brands.

### User Stories

All user stories can be found in the linked GitHub project [here](https://github.com/users/leec313/projects/3)

## Visual Design
### Wireframes

WIREFRAMES LINK HERE

### Fonts

- **Logo:** 
**[Protest Strike Font](https://fonts.google.com/specimen/Protest+Strike):** Protest Strike is a bold and impactful display font that adds a rebellious and edgy vibe to your project. With its strong, stencil-like appearance, Protest Strike commands attention and makes a statement, perfect for conveying a sense of activism or boldness in your design. Its distinct letterforms and unique style give your project a standout aesthetic, while still maintaining legibility for titles and headings.
**[Dancing Script Font](https://fonts.google.com/specimen/Dancing+Script):** Dancing Script is a playful and elegant script font that brings a touch of whimsy and sophistication to your project. With its flowing, cursive letterforms and graceful strokes, Dancing Script adds a sense of charm and personality to your design, making it ideal for conveying a sense of warmth and friendliness.
Both Protest Strike and Dancing Script were used for my logo - they excellently contrast each other. 
- **Clean Aesthetic: [Lato](https://fonts.google.com/specimen/Lato)** (used for the rest of my site) is a sans-serif font with a clean and modern aesthetic, making it suitable for a wide range of design applications. Its simplicity and readability contribute to a professional and polished look for the project.
- **Universal Legibility:** Choosing sans-serif as the backup ensures universal legibility, especially on screens and digital platforms. Sans-serif fonts are known for their clarity and readability, making them a reliable fallback option in case any issues arise with the primary or secondary font choices. I also used cursive as the backup font for Dancing Script in the logo. 


### Colors

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/pallette.png?raw=true" alt="colors">
</div>

In crafting the color palette for this project, I aimed to strike a perfect balance between vibrancy, clarity, and visual appeal. Let's delve into why each color was carefully chosen:

- **Black (#000000) for the Logo**: Black, being classic and versatile, provides a strong foundation for our logo. Its timeless appeal ensures that our brand identity stands out boldly against lighter backgrounds, guaranteeing excellent readability and visibility. Plus, black exudes professionalism and sophistication, aligning perfectly with our brand's ethos.
    
- **White (#FFFFFF) for the Background**: White serves as the canvas upon which all other colors and content come to life. Its clean and neutral nature creates a sense of spaciousness and cleanliness, enhancing readability and user experience. A white background exudes simplicity and elegance, perfectly complementing various design styles.
    
- **Teal/Green (#009970) for Buttons, Links, Headers, and Icons**: Teal or green tones, such as #009970, inject vibrancy and energy into our project. This color choice for buttons, links, and headers adds visual interest and directs users' attention to key elements. Moreover, it's associated with growth, harmony, and freshness, resonating positively with our audience and conveying a welcoming vibe.
    
- **Red (#DC3545) for Errors and Delete Buttons**: Red, particularly #DC3545, serves as a signal for alerts, warnings, or errors. Its darker hue maintains visibility while conveying a sense of urgency or caution. By using this color for error messages and delete buttons, we ensure that users take notice and proceed with care when necessary.
    

In essence, our color palette embodies simplicity and vibrancy, creating a visually appealing and user-friendly experience. The combination of classic black, pristine white, lively teal/green, and alerting red forms a cohesive design that effectively communicates our brand's message. This palette also allows our vibrant product and blog imagery to shine, creating a dynamic and engaging platform for our audience.

ChatGPT

## Agile Development

The journey of Fetch & Feast began with the establishment of a GitHub Projects Page, serving as the central hub for project management. This platform played a pivotal role in organizing tasks systematically, creating user stories, and breaking them down into actionable steps. The overarching goal was to create a structured roadmap that would guide the project towards successful completion within the designated timeframe. Utilizing the GitHub Projects Page enabled the tracking of the project's evolution, assignment of tasks, and achievement of milestones, ensuring a smooth and organized development process.

To view the:

* project Kanban board, [please follow this link.](https://github.com/users/leec313/projects/3)
* milestones, [please follow this link.](https://github.com/leec313/Fetch-and-Feast/milestones)
* issues, [please follow this link.](https://github.com/leec313/Fetch-and-Feast/issues?q=is%3Aissue)

### Project Milestones

The project was divided into several key milestones, each representing a significant phase in the development process. Within each milestone, epics were identified, representing broader themes or features to be implemented. These epics were further broken down into user stories, representing specific functionalities or requirements from the user's perspective. Finally, tasks were defined within each user story, representing the individual steps needed to fulfill the user story's objectives.

### Example Milestones, Epics, User Stories, and Tasks (not representative of the actual project):

1. **Milestone 1: Project Setup**
    
    - Epic 1: Repository Setup
        - User Story 1: Initialize Git repository
            - Task 1: Create repository on GitHub
            - Task 2: Clone repository locally
        - User Story 2: Setup Development Environment
            - Task 1: Install necessary dependencies
            - Task 2: Configure project settings
2. **Milestone 2: User Authentication**
    
    - Epic 2: User Registration
        - User Story 3: Allow users to register for an account
            - Task 1: Create user registration form
            - Task 2: Implement backend logic for user registration
        - User Story 4: Enable email verification for new accounts
            - Task 1: Generate verification email upon registration
            - Task 2: Implement email verification process
3. **Milestone 3: Product Management**
    
    - Epic 3: Product Listing
        - User Story 5: Display list of available products
            - Task 1: Design product listing page UI
            - Task 2: Fetch and display products from database
        - User Story 6: Implement product search functionality
            - Task 1: Create search bar component
            - Task 2: Implement search logic

### Project Progression

The project evolved iteratively, with each milestone representing a significant step forward in the development process. Tasks within each milestone were completed incrementally, with regular reviews and adjustments made to ensure alignment with project goals and user requirements. As tasks were completed, they were moved across the Kanban board, providing a clear visual representation of progress and remaining work.

In summary, the use of project milestones, epics, user stories, and tasks, coupled with effective project management tools like GitHub Projects and Kanban boards, facilitated a structured and organized approach to building Fetch & Feast.


## Features

### Existing Features

### Site Pages

- **Homepage**

- **Navigation Bar:**
    - The navigation bar serves as a central hub for accessing key features and navigating the site.
    - **Logo:**
        - Positioned prominently on the left side of the navigation bar, the logo serves as a visual anchor, reinforcing brand identity.
    - **Search Bar:**
        - Located prominently within the navigation bar, the search bar allows users to quickly find specific products or content.
    - **Account Dropdown:**
        - For logged-out users, the account dropdown provides options to log in or sign up for an account.
        - Logged-in users have access to their profile, enabling them to manage their account settings, view orders, and access additional features.
        - Superusers have additional options for product and blog management, allowing them to oversee content creation and updates.
    - **Main Navigation:**
        - Positioned below the account dropdown, the main navigation menu offers dropdown options for each page category, including Products, Blogs, Help, and More.
        - Each dropdown menu provides access to specific sections or pages related to the respective category, enhancing navigation efficiency for users.

- **Hero Image:**

    -  The main homepage features a large and visually striking hero image that immediately captures the user's attention.
    - A prominent call-to-action button invites users to enter and explore the site's products.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/hero-nav.png?raw=true" alt="hero-image-and-nav">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/hero-nav-mobile.png?raw=true" alt="hero-image-and-nav-mobile">
</div>

- **Featured Products:**
    
    - Below the hero image, four featured products are showcased.
    - These products are selected based on the highest average ratings, ensuring that users see the most popular items first.
    - A "View All" button allows users to easily access the full range of products available on the site.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/featured-products.png?raw=true" alt="featured-products">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/featured-products-mobile.png?raw=true" alt="featured-products-mobile">
</div>

- **Newsletter Sign-up Form:**
    
    - **For Logged-In Users:**
        - The newsletter sign-up process is seamlessly integrated with the user profile model.
        - Logged-in users are alerted if they attempt to sign up for the newsletter while already subscribed.
    - **For Anonymous Users:**
        - Anonymous users can also sign up for the newsletter by providing their email address.
        - Upon sign-up, a dummy user profile is created for them with only the email field added.
        - This is necessary to ensure proper linking between the newsletter model and user profile model.
        - If an anonymous user enters an email that is already subscribed, they are alerted via a toast alert.

- **Confirmation Process:**
    
    - Upon successful sign-up via the newsletter form, both the user and the site administrator receive email confirmations.
    - This confirmation email serves to confirm the subscription for the user and alert the admin about the new subscription.

- **Code Location:**
    
    - The implementation details for managing the newsletter sign-up process can be found in the `subscribe_newsletter` view within the `home` app.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/newsletter.png?raw=true" alt="newsletter-signup">
</div>

- **Featured Blogs:**
    
    - In addition to featured products, the homepage also highlights four curated blogs.
    - These blogs are selected based on their relevance and popularity, providing users with valuable insights and information.
    - A "View All" button allows users to explore the complete collection of blogs available on the site, encouraging further engagement with the content.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/featured-blogs.png?raw=true" alt="featured-blogs">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/featured-blogs-mobile.png?raw=true" alt="featured-blogs-mobile">
</div>

- **Footer:**
    
    - The footer section of the website offers convenient navigation and essential information for users.
    - **Help Column:**
        - Includes links to the contact page and FAQ section, providing users with quick access to assistance and support.
    - **My Account Column:**
        - For logged-out users, this column features options to log in or sign up for an account.
        - Logged-in users have access to their profile, allowing them to manage their account settings, and sign out if needed.
        - Superusers have additional options for product and blog management, enabling them to oversee content creation and updates.
    - **Pages Column:**
        - Provides easy access to product pages and blog sections, enhancing navigation efficiency for users.
    - **General Information:**
        - Includes essential contact details such as phone number, email address, and location, ensuring users can reach out for assistance or inquiries.
    - **Social Media and Legal Links:**
        - Features a link to the site's Facebook page, facilitating social media engagement and community interaction.
        - Includes copyright information and a link to the privacy policy, ensuring compliance with legal requirements and providing transparency to users regarding data usage and privacy practices.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/footer.png?raw=true" alt="footer">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/footer-mobile.png?raw=true" alt="footer-mobile">
</div>

- **Product List**
    - The product list feature provides users with a straightforward and intuitive way to browse through available products.
    - **Display Format:**
        - Products are presented in individual cards, each containing essential information such as the product image, name, rating, price, and category.
        - For superusers, additional options to edit and delete products are available directly within the product cards.
    - **Pagination:**
        - To enhance usability and manageability, the product list is paginated to display a maximum of 8 products per page.
        - If there are more than 8 products, a "Next" button appears at the bottom of the page, allowing users to navigate to additional pages of products seamlessly.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/products.png?raw=true" alt="products">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/products-mobile.png?raw=true" alt="products-mobile">
</div>

- **Product Detail**
    - The product detail section on the product page provides users with comprehensive information about the selected product.
    - **Content Displayed:**
        - Product Name: Clearly identifies the product for users.
        - Price: Displays the price of the product, allowing users to make informed purchasing decisions.
        - Average Rating: Shows the average rating of the product based on user reviews from the ratings model, providing social proof and credibility.
        - Category: Indicates the category to which the product belongs, aiding users in navigation and organization.
        - Edit/Delete Links (for Superusers): Allows superusers to perform administrative actions such as editing or deleting the product directly from the product detail page.
        - Product Description: Provides a detailed description of the product, highlighting its features and benefits.
        - Quantity Selector: Enables users to select the desired quantity of the product before adding it to their shopping bag.
        - "Keep Shopping" Button: Offers users the option to continue browsing other products without leaving the current page.
        - "Add to Bag" Button: Allows users to add the selected quantity of the product to their shopping bag, initiating the checkout process.
    - **Product Image:**
        - The product image is prominently displayed within the product detail section.
        - A simple Bootstrap popup modal is implemented to allow users to view a larger version of the product image if desired, enhancing the user experience by providing a closer look at the product.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/product-detail.png?raw=true" alt="products">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/product-detail-mobile.png?raw=true" alt="products-mobile">
</div>

- **Ratings (on Product Detail page)**

    - The `product_detail` view renders the ratings.
    - Ratings for the product are retrieved from the database and paginated for easy navigation.
    - Users can rate the product using a form, with validation to ensure proper input.
    - A check is performed to determine if the current user has previously purchased the product, allowing only verified purchasers to submit ratings.
    - Profile images of users who submitted ratings are displayed alongside their usernames, enhancing the credibility of the ratings.
    - Superusers have the ability to edit or delete individual ratings through dedicated update and delete views.
    - Pagination is implemented to manage large product lists, ensuring optimal performance and user experience.

    - **Forms and Views for Rating Manipulation:**
    
        - The `RatingUpdateView` and `RatingDeleteView` classes allow users to update or delete individual ratings.
        - Users can modify the title, body, or score of their existing ratings through the update view.
        - Upon successful update or deletion, users receive confirmation messages and are redirected to the corresponding product detail page.
        - Views are protected with authentication and authorization checks to ensure that only logged-in users with appropriate permissions can access rating manipulation functionalities.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/ratings.png?raw=true" alt="ratings">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/ratings-mobile.png?raw=true" alt="ratings-mobile">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/edit-rating.png?raw=true" alt="rating-edit">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/delete-rating.png?raw=true" alt="ratings-delete">
</div>

- **Blog List:**
    - The blog list feature offers users an organized view of available blogs, facilitating easy exploration of content.
    - **Display Format:**
        - Blogs are presented in individual cards, each comprising essential details such as the blog image, title, excerpt, creation date, number of likes, and comments.
        - For superusers, additional options to edit and delete blogs are embedded within the blog cards, providing efficient content management capabilities.
    - **Search Functionality:**
        - A search bar is integrated into the blog list, allowing users to perform keyword searches to find specific blogs of interest.
        - Users can enter search queries to filter blogs based on titles, content, or any relevant keywords, enhancing discoverability and accessibility of content.
    - **Pagination:**
        - To optimize user experience and navigation, the blog list is paginated to display a maximum of 6 blogs per page.
        - If the total number of blogs exceeds the limit, a "Next" button is provided at the bottom of the page, enabling users to seamlessly navigate to subsequent pages of blog entries.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blog-detail.png?raw=true" alt="blogs">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blog-detail-1.png?raw=true" alt="blogs-mobile">
</div>

- **Blog Detail:**
    - The blog detail view offers users a comprehensive presentation of an individual blog post, providing detailed insights into its content and context.
    - **Display Format:**
        - The blog title is prominently featured at the beginning of the page, ensuring clear identification and navigation for users.
        - An image accompanies the blog post, enhancing visual appeal and engagement. In case no uploaded image is available, a default placeholder image is utilized, maintaining consistency across the site.
        - The main body of the blog post content is displayed, offering users valuable information and insights.
        - A "Like" button allows users to express their appreciation for the blog post by submitting a like, contributing to user engagement and interaction.
        - The number of likes and comments associated with the blog post is prominently displayed, providing social proof and encouraging further engagement from users.
        - Information such as the creation date and author of the blog post is included, offering users context and credibility regarding the content.
        - Superusers have access to update and delete buttons, empowering them with content management capabilities directly from the blog detail view.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blog-detail.png?raw=true" alt="blog-detail">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blog-detail-1.png?raw=true" alt="blog-detail-1">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blog-detail-mobile.png?raw=true" alt="blog-detail-mobile">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blog-detail-mobile-1.png?raw=true" alt="blog-detail-mobile-1">
</div>

- **Comment Section:**
    - The comment section provides users with a platform to engage in conversations and share their thoughts on the blog post, fostering communication and connection within the community.
    - **Display Format:**
        - Comments are presented in a Facebook Messenger-style display, offering a familiar and intuitive interface for users to interact with.
        - Each comment includes essential details such as the commenter's name, profile image, comment content, timestamp, and options for editing or deleting their own comments.
        - Pagination is implemented to manage large volumes of comments effectively, ensuring seamless navigation and optimal performance. AJAX technology is utilized to enable pagination without reloading the entire page, enhancing user experience and reducing load times.
    - **Functionality:**
        - Users can submit comments on the blog post, enabling them to contribute to the conversation and share their perspectives.
        - Comments are stored in the comment model within the database, ensuring data integrity and accessibility for future reference.
        - Commenters have the ability to edit or delete their own comments, empowering them with control over their contributions to the discussion.
    - **Engagement:**
        - The comment section serves as a valuable tool for user engagement, allowing readers to interact with the blog post content and with each other, fostering a sense of community and connection.
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/comments.png?raw=true" alt="comments">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/comments-mobile.png?raw=true" alt="comments-mobile">
</div>

- **Post Update:**
    - The post update functionality enables users to modify existing blog posts, providing flexibility and control over content management.
    - **Implementation:**
        - Post updates are facilitated through a dedicated form, `PostForm`, defined within the blogs app's `forms.py`.
        - To enhance user experience and streamline content creation, the rich text editor TinyMCE is integrated into the form for formatting the content. This implementation allows users to apply various text formatting options, insert multimedia elements, and customize the appearance of their blog post content effortlessly.
        - The integration of TinyMCE is achieved by including the necessary JavaScript and configuration settings within the HTML templates where the `PostForm` is rendered. This enables the rich text editor to be seamlessly embedded into the form, providing a familiar and intuitive editing experience for users.
    - **Editable Fields:**
        - Users have the ability to edit multiple fields within the blog post, including the title, content, excerpt, and image.
        - The `PostForm` dynamically populates the form fields with the existing data from the corresponding fields in the `Post` model, allowing users to make precise modifications to their blog posts.
    - **User Interface:**
        - The post update interface presents users with a structured form layout, clearly indicating the fields available for editing and providing descriptive labels and input fields for ease of use.
        - Upon submission of the updated post, the form validates the user input to ensure data integrity and consistency, providing feedback on any errors or invalid entries encountered during the editing process.
- **Post Delete Confirmation:**
    - The post delete confirmation process shares similarities with the ratings delete confirmation in terms of its functionality and user interaction. See Ratings Delete COnfirmation screenshot above for reference. 
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/post-update.png?raw=true" alt="post-update">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/post-update-mobile.png?raw=true" alt="post-update-mobile">
</div>

- **Contact Page:**
    - The contact page serves as a communication gateway for users to connect with the platform administrators, facilitating inquiries, feedback, and support requests.
    - **Contact Form:**
        - The central feature of the contact page is a user-friendly contact form, designed to capture essential information from users and streamline the communication process.
        - The contact form includes fields for the user's name, email address, subject, and message, allowing users to provide detailed information regarding their inquiry or feedback.
        - The subject field is implemented as a dropdown menu, presenting users with predefined options such as complaint, feedback, returns, shipping, and other. This structured approach helps categorize and prioritize incoming messages, enabling administrators to address user queries more efficiently.
    - **Functionality:**
        - Upon submission of the contact form, the contact view, located within the `fetch-and-feast` app's `views.py`, processes the user's input and initiates the necessary actions to handle the contact request.
        - Confirmation Emails:
            - Upon receiving a contact message, users are sent a confirmation email acknowledging the receipt of their message, providing reassurance and setting expectations for further communication.
            - Simultaneously, the platform administrators receive an email notification containing the user's contact information, selected subject, and message content. This email notification ensures prompt attention to user inquiries and facilitates timely responses.
    - **User Interface:**
        - The contact form interface is designed with simplicity and clarity in mind, featuring intuitive input fields and clear labels to guide users through the form submission process.
        - Dropdown menus and input validation mechanisms are employed to enhance user experience and ensure the accuracy of submitted information, minimizing errors and improving data quality.
    - **Email Notifications:**
        - Email notifications generated by the contact form submission process adhere to predefined templates and messaging guidelines, providing consistent communication and branding across all user interactions.
        - The inclusion of relevant contact details and message content in email notifications enables administrators to quickly grasp the nature of the user's inquiry and respond accordingly, facilitating efficient resolution of user issues and inquiries.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/contact.png?raw=true" alt="contact">
</div>

- **FAQ Page:**
    - The FAQ (Frequently Asked Questions) page serves as a comprehensive resource for addressing common inquiries and concerns users may have regarding various aspects of the platform's services and policies.
    - **Page Structure:**
        - The FAQ page adopts a structured format, presenting a series of questions and corresponding answers in an accordion-style layout. This format allows users to easily navigate through the FAQ sections and access relevant information efficiently.
    - **Content Organization:**
        - Each FAQ entry is encapsulated within a collapsible card element, with the question serving as the card header and the answer concealed within the collapsible body.
        - Users can expand or collapse individual FAQ entries by clicking on the associated question button, enhancing the user experience by providing interactive access to information.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/faqs.png?raw=true" alt="faqs">
</div>

- **Profile Page:**
    - The profile page serves as a personalized dashboard for registered users, providing access to essential account management functionalities and order history details.
    - **Page Structure:**
        - The profile page is structured to display user-specific information, including personal details, order history, and options for profile customization.
        - Components such as user profile forms, password change forms, and newsletter subscription settings are integrated seamlessly within the page layout to facilitate user interaction and account management.
    - **User Profile Section:**
        - User profile information, including username, email, first name, and last name, is presented within dedicated form fields, allowing users to update their personal details conveniently.
        - Profile updates are processed asynchronously, enabling users to modify their information without interrupting their browsing experience.
    - **Password Change Functionality:**
        - Users can initiate password changes directly from the profile page by accessing the password change form.
        - The password change process is handled securely, with validation checks to ensure the accuracy and integrity of the updated password.
    - **Order History Display:**
        - The profile page includes a dedicated section for displaying order history details, providing users with comprehensive insights into their past purchases and transaction history.
        - Each order entry is presented in a clear and organized manner, showcasing essential order information such as order number, date, and item details.
    - **User Interaction and Feedback:**
        - Feedback messages are incorporated throughout the profile page to notify users of successful profile updates, password changes, or any encountered errors during the process.
        - User-friendly messaging enhances the overall user experience and fosters a sense of confidence and satisfaction in utilizing the platform's account management features.

- **Newsletter Subscription Management on the Profile Page:**
    - Newsletter subscription management is a key feature integrated into user profiles, allowing users to opt in or out of receiving periodic newsletters and updates from the platform.
    - **User Profile Integration:**
        - The newsletter subscription functionality is seamlessly integrated with the user profile model (`UserProfile`), enhancing the platform's account management capabilities.
        - Within the `UserProfile` model, a boolean field named `subscribe_newsletter` is provided to track the user's newsletter subscription status.
        - When a user subscribes to the newsletter, the `subscribe_newsletter` field is set to `True`, indicating their preference to receive newsletters.
    - **Newsletter Subscription Model:**
        - The `NewsletterSubscription` model defines the structure for storing newsletter subscription details, including the associated user profile, email address, and creation timestamp.
        - Each newsletter subscription entry is linked to a specific user profile, establishing a direct relationship between user accounts and subscription preferences.
        - An `unsubscribe_token` field is included to generate a unique identifier for managing unsubscribe requests securely and for dealing with anonymous users without a profile/account.
    - **Newsletter Unsubscribe Functionality:**
        - To ensure consistency and data integrity, a signal (`pre_delete`) is implemented to update the user profile's `subscribe_newsletter` field when a newsletter subscription is deleted.
        - The signal handler (`update_user_profile_on_newsletter_delete`) automatically sets the `subscribe_newsletter` field to `False` when a subscription is removed, reflecting the user's updated preferences accurately.
    - **Opt-in/Opt-out Mechanism:**
        - Users can modify their newsletter subscription preferences directly from their profile page, toggling the subscription checkbox to subscribe or unsubscribe as desired.
        - When a user subscribes to the newsletter, a new `NewsletterSubscription` entry is created, associating the subscription with the user's profile and email address.
        - Conversely, if a user chooses to unsubscribe, the corresponding `NewsletterSubscription` entry is deleted, and the `subscribe_newsletter` field in the user profile is updated accordingly, ensuring synchronization between user preferences and subscription status.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/profile.png?raw=true" alt="profile">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/profile-mobile.png?raw=true" alt="profile-mobile">
</div>
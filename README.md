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

     <li><details>
    <summary><a href="#agile-development">Agile Development</a></summary>

    - [Milestones](#project-milestones)
    - [Progression](#project-progression)
    </details></li>

    </ul>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#site-pages">Site Pages</a></summary>

    - [Homepage](#homepage)
    - [Newsletter Subscription Popup](#newsletter-subscription-popup)
    - [Footer](#footer)
    - [Product List](#product-list)
    - [Product Detail](#product-detail)
    - [Ratings](#ratings)
    - [Blog List](#blog-list)
    - [Blog Detail](#blog-detail)
    - [Comment Section](#comment-section)
    - [Post Update](#post-update)
    - [Contact Page](#contact-page)
    - [FAQ Page](#faq-page)
    - [Profile Page](#profile-page)
    - [Newsletter Subscription Management](#newsletter-subscription-management)
    - [Bag Page](#bag-page)
    - [Toasts Including Bag Preview](#toasts-including-bag-preview)
    - [Product Management](#product-management)
    - [Blog Management](#blog-management)
    - [Checkout](#checkout)
    - [Checkout Success](#checkout-success)
    - [Authentication Pages](#authentication-pages)    
    </details></li>

    <li>
    <a href="#features-not-yet-implemented">Features Not Yet Implemented</a>
    </li>
    </ul>
</details>

3. <summary><a href="#technologies-used">Technologies Used</a></summary>

4. <summary><a href="#webhooks">Webhooks</a></summary>

5. <summary><a href="#database-design">Database Design</a></summary>

6. <summary><a href="#ecommerce-business-model">Ecommerce Business Model</a></summary>

7. <summary><a href="#search-engine-optimization-and-social-media-marketing">Search Engine Optimization And Social Media Marketing
</a></summary>

8. <details open>
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

9. <a href="#deployment">Deployment</a>

10. <a href="#credits-and-acknowledgements">Credits and Acknowledgements</a>

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

## Agile Development

The journey of Fetch & Feast began with the establishment of a GitHub Projects Page, serving as the central hub for project management. This platform played a pivotal role in organizing tasks systematically, creating user stories, and breaking them down into actionable steps. The overarching goal was to create a structured roadmap that would guide the project towards successful completion within the designated timeframe. Utilizing the GitHub Projects Page enabled the tracking of the project's evolution, assignment of tasks, and achievement of milestones, ensuring a smooth and organized development process. The MoSCoW method, alongside customized GitHub project labels, was instrumental in assisting me in prioritizing essential tasks within the constraints of my available time.

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

- ### Homepage

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

- ### Newsletter Subscription Popup

    This feature enhances user engagement by displaying a newsletter subscription popup five seconds after the page loads. Here's how it works:

    - **Modal Display:** The popup modal is triggered to appear after a brief delay, providing users with an opportunity to subscribe to the newsletter.
    - **Cookie Management:** Once the modal is shown to the user, a cookie is set to prevent the popup from appearing again during subsequent visits or page refreshes.
    - **User Interaction:** Users can choose to close the modal by clicking outside of it or submitting their email address. Upon submission, the modal is closed, ensuring a seamless user experience.
    - **Backend Integration:** The logic for managing the newsletter subscription popup is implemented in the `newsletter_subscribe` view within the `home` app, facilitating smooth integration with the application's backend functionality.

    This approach optimizes user interaction while respecting user preferences and privacy by controlling the frequency of the newsletter subscription popup display.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/newsletter-popup.png?raw=true" alt="newsletter-popup">
</div> 

- ### Footer
    
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

- ### Product List
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

- ### Product Detail
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

- ### Ratings

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

- ### Blog List
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
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blogs.png?raw=true" alt="blogs">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blog-mobile.png?raw=true" alt="blog-mobile">
</div>

- ### Blog Detail
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

- ### Comment Section
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

- ### Post Update
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

- ### Contact Page
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

- ### FAQ Page
    - The FAQ (Frequently Asked Questions) page serves as a comprehensive resource for addressing common inquiries and concerns users may have regarding various aspects of the platform's services and policies.
    - **Page Structure:**
        - The FAQ page adopts a structured format, presenting a series of questions and corresponding answers in an accordion-style layout. This format allows users to easily navigate through the FAQ sections and access relevant information efficiently.
    - **Content Organization:**
        - Each FAQ entry is encapsulated within a collapsible card element, with the question serving as the card header and the answer concealed within the collapsible body.
        - Users can expand or collapse individual FAQ entries by clicking on the associated question button, enhancing the user experience by providing interactive access to information.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/faqs.png?raw=true" alt="faqs">
</div>

- ### Profile Page
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

- ### Newsletter Subscription Management
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


- ### Bag Page
    - Overall, the bag page serves as a pivotal stage in the user's journey through the e-commerce platform, offering transparency, control, and convenience in managing their selected items before finalizing their purchase.
    - **Add to Bag Function:**
        - The `add_to_bag` function enables users to add a specified quantity of a product to their shopping bag.
        - Upon receiving a POST request, the function retrieves the product details, including its size if applicable, and updates the bag session accordingly.
        - Messages are displayed to inform the user about the action taken, such as adding a new item or updating the quantity of an existing item.
    - **Adjust Bag Function:**
        - The `adjust_bag` function allows users to adjust the quantity of a product already present in their bag.
        - Users can modify the quantity of the product and update the bag session accordingly, with appropriate messages displayed to confirm the action.
        - Additionally, users can adjust the quantity of products based on their size if applicable.
    - **Remove from Bag Function:**
        - Users have the option to remove items from their shopping bag using the `remove_from_bag` function.
        - Upon receiving a POST request, the function removes the specified item from the bag session, considering the item's size if provided, and updates the bag accordingly.
        - Success messages are displayed to notify users about the successful removal of items from their bag.
    - **Empty Bag Function:**
        - The `empty_bag` function allows users to clear all items from their shopping bag in a single action.
        - Upon invocation, the function clears the bag session entirely, ensuring that no items remain in the user's bag.
        - Users receive a success message confirming that their bag has been emptied, providing a seamless shopping experience.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/bag.png?raw=true" alt="bag">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/bag-mobile.png?raw=true" alt="bag-mobile">
</div>

- ### Toasts Including Bag Preview

Toast Messages play a crucial role in providing real-time feedback to users regarding the outcome of their actions on the e-commerce platform. Here's an overview of the Toast Messages implementation:

- **Purpose:**
    
    - Toast Messages are utilized to inform users about the completion of various actions, such as successful login, product deletion, and other important events.
    - They serve as non-intrusive notifications that appear briefly on the screen, ensuring users are promptly informed without interrupting their browsing experience.
- **Implementation:**
    
    - The platform employs a standardized toast template, ensuring consistency in appearance and functionality across different scenarios.
    - Specifically, the toast success template is utilized for the bag preview popup, maintaining visual coherence and reinforcing positive feedback for successful bag updates.
    - JavaScript is integrated to control the behavior of toast messages. By default, all toast messages automatically disappear after three seconds, enhancing user experience by minimizing clutter.
    - However, toast messages associated with the class bag-notification-wrapper remain persistent until the user takes action, such as clicking the close button. This approach enables users to review bag-related notifications at their own pace without fear of them disappearing prematurely.
- **User Interaction:**
    
    - Upon receiving a toast message, users can take appropriate actions based on the context provided.
    - For example, if a toast message indicates successful addition or removal of items from the bag, users may choose to continue shopping, proceed to the bag page, or directly navigate to the checkout process.
    - The inclusion of action buttons or links within toast messages enhances user control and facilitates seamless navigation through the platform.

Overall, Toast Messages serve as an integral component of the platform's user interface, enhancing user satisfaction and facilitating smooth interactions by providing timely feedback on important actions and events.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/toast.png?raw=true" alt="toast">
</div>

- ### Product Management
    - **Purpose:**
        
        - The Product Management Page is designed exclusively for superusers to oversee and manage products within the e-commerce platform.
        - It serves as a centralized hub for performing various product-related tasks, including deletion, addition, editing, and category management.
        - The page offers enhanced functionality such as bulk-delete options, search capabilities, and pagination to streamline product management processes.
    - **Features:**
        
        - **Bulk Delete:** Superusers have the ability to select multiple products for deletion simultaneously, streamlining the process of removing outdated or unnecessary items from the inventory.
        - **Add Products:** Superusers can easily add new products to the platform, providing essential details such as SKU, name, price, image, and category to enrich the product catalog.
        - **Edit Products:** Existing product information can be modified and updated as needed, empowering administrators to keep product details accurate and up to date.
        - **Add Product Categories:** Superusers have the flexibility to create and assign new categories to products, facilitating organization and navigation within the product catalog.
        - **Search Functionality:** A search bar is available to facilitate quick and efficient retrieval of specific products based on user-defined criteria, enhancing usability and productivity.
        - **Table Format:** Product information is presented in a structured table format, ensuring clarity and ease of navigation. Each row includes essential details such as database ID, product image, SKU, name, availability of sizes, price, and average rating.
        On Mobile, some columns have been removed to prevent horizontal scrolling.
        - **Select All Checkbox:** Superusers can conveniently select all products displayed on the page using a single checkbox, enhancing efficiency when performing bulk actions. This functionality is implemented using JavaScript for seamless user interaction.
        - **Pagination:** To manage large datasets effectively, pagination is implemented with a maximum of 8 products per page. This ensures optimal performance and navigational convenience for administrators.
    - **User Interaction:**
        
        - Superusers can navigate through the product list, search for specific products, and perform various actions such as editing, deleting, or adding products with ease.
        - The select all checkbox simplifies the process of selecting multiple products for bulk actions, enhancing productivity and efficiency.
        - Interactive elements such as dropdown menus, input fields, and buttons provide intuitive controls for managing products and categories seamlessly.
        - Pagination controls allow superusers to navigate through multiple pages of product listings effortlessly, ensuring a smooth user experience even with a large number of products.

    Overall, the Product Management Page empowers superusers with comprehensive tools and features to effectively manage and maintain the product inventory, contributing to the overall success and efficiency of the e-commerce platform.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/product-manage.png?raw=true" alt="product-manage">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/product-manage-mobile.png?raw=true" alt="product-manage-mobile">
</div>

- ### Blog Management

    - **Purpose:**
        
        - Similar to the Product Management Page, the Blog Management Page, exclusively accessible to superusers, serves as the central hub for overseeing and managing blog content within the platform.
        - It offers essential functionality for editing, deleting, and reviewing detailed information about each blog post, ensuring the platform's blog remains dynamic and relevant.
    - **Features:**
        
        - **Edit and Delete:** Superusers can effortlessly modify existing blog posts or remove outdated content, maintaining the blog's freshness and relevance.
        - **Blog Information:** Each post is presented in a structured table format, displaying key details such as database ID, blog image, title, author, creation date, comments count, and likes count.
        - **Select Box:** Interactive select boxes enable superusers to perform actions like editing or deleting specific blog posts, providing intuitive controls for efficient management.
        - **Blog Image:** Visual representations aid in quickly identifying and managing posts based on their associated images.
        - **Author and Date:** Detailed information about each post, including the author's name and creation date, facilitates oversight and management.
        - **Comments and Likes:** Insights into engagement levels, including total comments and likes received, help gauge the popularity and impact of individual posts.
        - **Search Functionality:** A search bar allows for quick retrieval of specific posts based on user-defined criteria, enhancing usability and productivity.
        - **Pagination:** Pagination is implemented for effective management of large datasets, ensuring optimal performance and navigational convenience.
    - **User Interaction:**
        
        - Superusers can interact with blog posts directly from the management page, with options to edit, delete, or view detailed information.
        - The structured table format presents content clearly, enabling quick assessment and management based on specific attributes.
        - Interactive select boxes and search functionality enhance user experience, providing intuitive controls for navigation and management.
        - Insights into comments and likes assist superusers in understanding audience response, informing future content strategies.

    Overall, the Blog Management Page equips superusers with essential tools to oversee and maintain blog content effectively, ensuring the platform remains engaging and relevant for users.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/blog-manage.png?raw=true" alt="blog-manage">
</div>

- ### Checkout

    - **Purpose:**
        
        - The Checkout Page serves as the final step in the online purchasing process, where customers review their order details, provide shipping and payment information, and complete their transactions.
    - **Features:**
        
        - **Order Summary:** Displays a summary of the items in the customer's shopping bag, including product names, quantities, prices, and total cost.
        - **Checkout Form:** Allows customers to enter shipping details such as full name, email, phone number, shipping address, and payment information through a user-friendly form.
        - **Payment Processing:** Utilizes the Stripe API for secure payment processing, ensuring that customer transactions are handled securely and efficiently.
        - **Order Creation:** Upon successful completion of the checkout process, creates an order with relevant details, including product information, payment ID, and customer information.
        - **Checkout Success Handling:** Handles successful order processing, displaying confirmation messages to customers and providing order details for reference.
        - **Save Information Option:** Provides customers with the option to save their shipping information for future purchases, enhancing convenience and streamlining the checkout process for returning customers.
    - **User Interaction:**
        
        - Customers interact with the Checkout Page to review and confirm their order details, enter shipping information, and complete their purchases securely.
        - Seamless navigation and intuitive form design contribute to a positive user experience, ensuring customers can complete transactions efficiently.
        - Upon successful checkout, customers receive confirmation messages indicating successful order processing and providing order numbers for reference.

    The Checkout Page plays a crucial role in facilitating smooth and secure transactions, providing customers with a convenient and reliable platform for completing their online purchases.

- ### Checkout Success Page

    - **Purpose:**
        
        - The Checkout Success Page confirms successful order processing to customers, providing essential order details and serving as a receipt for completed transactions.
    - **Features:**
        
        - **Order Confirmation:** Displays a confirmation message to customers, indicating that their order has been successfully processed.
        - **Order Details:** Provides customers with comprehensive order details, including order number, itemized list of purchased products, total cost, and shipping information.
        - **Cookie Implementation:** Utilizes a custom cookie, specific to each user, to ensure secure access to the Checkout Success Page. This cookie prevents unauthorized access and ensures that only the customer who completed the transaction can view the success page.
        - **Order Completion:** Marks the successful completion of the checkout process, allowing customers to proceed with confidence knowing that their order has been successfully placed.
    - **User Interaction:**
        
        - Upon successful order completion, customers are directed to the Checkout Success Page, where they receive confirmation messages and detailed order information.
        - The custom cookie implemented on the success page ensures secure access, restricting page access to the specific user who completed the transaction.
        - Customers can review their order details, verify the accuracy of their purchases, and refer to the order number for future inquiries or tracking purposes.

    The Checkout Success Page provides customers with reassurance and confidence that their orders have been successfully processed, while the implementation of a custom cookie ensures the security and privacy of their transaction information.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/checkout.png?raw=true" alt="checkout">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/success.png?raw=true" alt="success">
</div>

- ### Authentication Pages

    - **Purpose:**
        
        - The authentication pages serve as entry points for users to create accounts, log in, and manage their passwords securely.
    - **Features:**
        
        - **Signup Page:**
            - Allows new users to create accounts by providing necessary information such as username, email, and password.
            - Utilizes Django Allauth for streamlined signup process, offering features like email verification and social media authentication options.
            - Validates user input to ensure data accuracy and compliance with security standards.
        - **Login Page:**
            - Provides existing users with a secure gateway to access their accounts by entering their credentials.
            - Supports username/email and password authentication, offering a smooth login experience.
            - Utilizes Django Allauth for enhanced login functionalities, including remember me option and password reset.
        - **Password Management:**
            - Includes password reset and change functionalities to enable users to manage their account security effectively.
            - Offers password reset via email, allowing users to regain access to their accounts in case of forgotten passwords.
            - Implements secure password change mechanisms to ensure user account integrity and prevent unauthorized access.
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/signup.png?raw=true" alt="signup">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/login.png?raw=true" alt="login">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/password.png?raw=true" alt="password">
</div>

# Features Not Yet Implemented

1. **Social Media Integration:**
    
    - **Purpose:**
        - Increase brand visibility and user engagement by allowing customers to share their experiences and product reviews on social media.
    - **Features:**
        - **Share Buttons:** Incorporate social media share buttons on product pages, order confirmation pages, and customer reviews, allowing users to share their experiences with Fetch & Feast products.
        - **User-Generated Content:** Encourage users to share photos of their dogs enjoying Fetch & Feast products, creating a community-driven approach to marketing.
        - **Integration with Social Platforms:** Seamlessly integrate sharing functionalities with popular social media platforms such as Facebook, Instagram, and Twitter to maximize reach and engagement.

2. **Subscription Box Service:**
    
    - **Purpose:**
        - Provide customers with a convenient and exciting way to receive a curated selection of dog treats, food, toys, and accessories on a recurring basis.
    - **Features:**
        - **Monthly Subscription Options:** Offer monthly subscription plans with customizable preferences based on the customer's dog size, dietary restrictions, and toy preferences.
        - **Curated Selection:** Curate each subscription box with a variety of high-quality products tailored to the customer's preferences, ensuring a delightful unboxing experience.
        - **Automated Billing and Shipping:** Automate billing and shipping processes for subscription boxes, providing hassle-free delivery to customers' doorsteps each month.

3. **Local Dog Park Finder:**
    
    - **Purpose:**
        - Enhance the platform's utility by helping users find nearby dog parks, grooming services, and pet-friendly establishments.
    - **Features:**
        - **Location-Based Search:** Implement a location-based search feature that allows users to find nearby dog parks and pet-friendly places based on their current location or specified area.
        - **Map Integration:** Integrate maps and navigation functionalities to provide users with directions to their selected dog parks or pet-friendly locations.
        - **Reviews and Ratings:** Enable users to leave reviews and ratings for dog parks and pet-friendly establishments, helping other users make informed decisions.

4. **Tailored Recommendations:**
    
    - **Purpose:**
        - Enhance the user experience by providing personalized product recommendations based on individual preferences and browsing history.
    - **Features:**
        - **Machine Learning Algorithms:** Utilize machine learning algorithms to analyze user behavior, purchase history, and preferences, then generate personalized product recommendations.
        - **Recommendation Engine:** Implement a recommendation engine that suggests relevant products to users based on their past interactions with the platform and similar users' preferences.
        - **Dynamic Recommendations:** Continuously update and refine product recommendations based on user feedback and evolving preferences.

5. **Wishlist Functionality:**
    
    - **Purpose:**
        - Allow users to create and manage wishlists of products they're interested in purchasing in the future, increasing user engagement and providing valuable insights into popular products.
    - **Features:**
        - **User-Specific Wishlists:** Enable users to create multiple wishlists and organize them according to their preferences, such as treats, toys, or grooming products.
        - **Save for Later:** Provide users with the option to move products from their shopping bag to their wishlist for future consideration, simplifying the purchase decision process.
        - **Share Wishlists:** Allow users to share their wishlists with friends and family, facilitating gift-giving and promoting user engagement.

6. **Contact Us Model with Admin Panel:**
    
    - **Purpose:**
        - Enhance user engagement and support by implementing a contact us model that stores user inquiries in a database.
    - **Features:**
        - **Database Integration:** Store user contact information, inquiries, and messages in a structured database, allowing for easy access and management.
        - **Admin Panel:** Provide administrators with a frontend contact management page where they can view, respond to, and manage user messages.
        - **Message Status:** Similar to Zendesk, allow admins to mark messages as solved or unresolved, helping track the status of user inquiries and ensuring timely responses.

7. **FAQ Model with Admin Panel:**
    
    - **Purpose:**
        - Improve user experience and provide a centralized platform for managing frequently asked questions.
    - **Features:**
        - **Database-Driven FAQ:** Implement a database-driven FAQ model that allows admins to add, archive, publish, and update FAQs directly from a frontend management page.
        - **Category Organization:** Enable admins to categorize FAQs for easier navigation and user access.
        - **Search Functionality:** Incorporate a search feature that allows users to quickly find relevant FAQs based on keywords or topics of interest.
        - **Version Control:** Maintain version control for FAQs, allowing admins to track changes and revert to previous versions if needed.

8. **Auto-Refill Subscriptions:**
    
    - **Purpose:**
        - Offer convenience and encourage customer loyalty by allowing users to set up automatic refills for their favorite dog treats or food at specified intervals.
    - **Features:**
        - **Recurring Purchase Options:** Enable users to subscribe to auto-refill options for specific products, selecting the frequency of delivery (e.g., weekly, monthly).
        - **Customizable Preferences:** Allow users to customize their auto-refill subscriptions based on their dog's dietary needs, portion sizes, and delivery preferences.
        - **Flexible Management:** Provide users with the flexibility to modify, pause, or cancel their auto-refill subscriptions at any time through their account dashboard.

9. **Pet Profile Management:**
    
    - **Purpose:**
        - Enhance personalization and recommendation accuracy by allowing users to create profiles for their pets, including details such as breed, age, and dietary preferences.
    - **Features:**
        - **Pet Profiles:** Enable users to create and manage profiles for each of their pets, providing information such as name, breed, age, weight, and any dietary restrictions.
        - **Personalized Recommendations:** Utilize pet profile data to tailor product recommendations based on each pet's specific needs, preferences, and health requirements.
        - **Health Tracking:** Offer features for users to track their pet's health and wellness metrics, such as activity levels, weight management, and vaccination schedules.

10. **Live Chat Support:**
    - **Purpose:**
        - Offer real-time assistance to users navigating the platform, answering queries, resolving issues, and providing personalized recommendations.
    - **Features:**
        - **Live Chat Widget:** Implement a chat widget that allows users to initiate conversations with customer support representatives while browsing the website.
        - **Multi-agent Support:** Enable multiple customer support agents to handle concurrent chat sessions, ensuring prompt responses during peak hours.
        - **Chatbot Integration:** Integrate a chatbot to handle frequently asked questions and basic inquiries, freeing up human agents to focus on more complex issues.
        - **Transcripts and History:** Provide users with access to chat transcripts and history for reference, enhancing the continuity of support interactions.
    - **Benefits:**
        - Enhances customer satisfaction by offering immediate assistance and personalized support.
        - Reduces cart abandonment rates by addressing user concerns and uncertainties in real-time.
        - Improves overall user experience by providing a seamless channel for communication and problem resolution.

# Technologies Used

### Html

 - Used to structure my webpages and the base templating language

### CSS

 - Custom CSS was written on large chunks of this site to make it as close to the wireframes as I felt it needed to be

### JavaScript

 -  Used to add timeout function for messages as well as to enable the menu on index.html

### Python

 -  Used for the logic in this project

### Django

 -  Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient

### Font Awesome

 -  Used for some icons throughout the project

### Bootstrap

 - Used as the base front end framework to work alongside Django. Also used Bootstrap icons in certain areas

### Jinja Templating with Django

 - Used to render logic within html documents and make the website more dynamic

### GitHub

 - Used to store the code for this project & for the projects Kanban board used to complete it

### Heroku

- Used to host and deploy this project

### ElephantSQL

- Used as the Postgres database

### Gunicorn

- Used for WSGI server

### Crispy Forms

- Used for auto-formatting of front-end forms

### TinyMCE

- Used for blog content formatting

### Allauth

- Used as the user authentication system

### AWS

- Used for hosting static and media files

### Git

- Used for version control throughout the project and to ensure a good clean record of work done was maintained

### Gitpod

- Used as IDE to develop the project

### Stripe

- Used for payment processing including webhooks

### ChatGPT 

- Assisted in formatting certain sections of this README and helped with certain Flake8 warnings throughout the project

### Leonardo.ai

- Used for various images throughout the site such as hero image, product images and most blog images. For some blog images, I used images taken by myself or friends. 

### Balsamiq Wireframe Program

- Used for the creation of wireframes

### xconvert.com

- Used for converting and condensing images to webp format

### Facebook

- Used for the creaton of the business page

### Wordtracker.com

- Used to conduct keyword research for SEO

### XML-Sitemaps

- Used to generate the sitemap

# Webhooks
    
- The site uses a secure and robust webhook system to ensure that the payment process cannot be interrupted and corrupted, either through user error or malicious intent. Webhooks are incorporated via the Stripe payment system and are handled on the Stripe website, by way of the python code in `checkout > webhook_handler.py` and `checkout > webhooks.py`

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/stripe.png?raw=true" alt="stripe-webhooks">
</div>


# Database Design

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/database.png?raw=true" alt="database">
</div>

1. **User (allauth)**:
    
    - This model represents a user account and is likely provided by Django's authentication system (allauth).
    - It serves as a base user model and is referenced by other models through foreign keys (FK), such as UserProfile, NewsletterSubscription, Order, Rating, and Comment.
2. **UserProfile**:
    
    - This model stores additional information about each user.
    - It has a one-to-one relationship with the User model, meaning each UserProfile instance is associated with exactly one User instance.
    - It contains fields like default\_email, default\_phone\_number, default\_street\_address1, etc., to store user-specific information.
3. **Product**:
    
    - This model represents a product available on the platform.
    - It has a foreign key (FK) relationship with the Category model, indicating that each product belongs to a specific category.
    - It's referenced by the OrderLineItem model through a foreign key, indicating that each order line item is associated with a specific product.
4. **NewsletterSubscription**:
    
    - This model represents a user's subscription to the newsletter.
    - It has a foreign key (FK) relationship with the UserProfile model, indicating that each subscription is associated with a specific user's profile.
5. **Order**:
    
    - This model represents an order placed by a user.
    - It has a foreign key (FK) relationship with the UserProfile model, indicating that each order is associated with a specific user's profile.
    - It's referenced by the OrderLineItem model through a foreign key, indicating that each order line item is associated with a specific order.
6. **Post**:
    
    - This model represents a post on the platform.
    - It has a foreign key (FK) relationship with the User model, indicating the author of the post.
    - It's referenced by the Comment model through a foreign key, indicating that each comment is associated with a specific post.
7. **Rating**:
    
    - This model represents a rating given by a user to a product.
    - It has foreign key (FK) relationships with both the Product and User models, indicating the product being rated and the user who gave the rating.
8. **OrderLineItem**:
    
    - This model represents a line item within an order.
    - It has foreign key (FK) relationships with both the Order and Product models, indicating the order the line item belongs to and the product being ordered.
9. **Category**:
    
    - This model represents a category for products.
    - It's referenced by the Product model through a foreign key, indicating that each product belongs to a specific category.
10. **Comment**:
    
    - This model represents a comment on a post.
    - It has foreign key (FK) relationships with both the Post and User models, indicating the post being commented on and the user who made the comment.

# Ecommerce Business Model

1. **Business Type**: Business to Customer (B2C)
    
2. **Nature of Business**: Fetch & Feast operates as an e-commerce platform specializing in the sale of dog treats, food, and toys to individual customers.
    
3. **Revenue Streams**:
    
    - Sales Revenue: Generated through the direct sale of dog treats, food, and toys to customers.
    - Advertising Revenue: Potential income from sponsored content or advertisements displayed on the website.
    - Partnership Revenue: Collaborations with pet-related brands or organizations for promotional activities.
4. **Customer Segments**:
    
    - Dog Owners: Individuals who own dogs and are interested in purchasing high-quality treats, food, and toys for their pets.
    - Pet Enthusiasts: Individuals passionate about pets who may purchase items for their own pets or as gifts for others.
5. **Value Proposition**:
    
    - Quality Products: Offering a wide range of high-quality dog treats, food, and toys sourced from reputable suppliers.
    - Convenience: Providing a convenient online platform for customers to browse, purchase, and receive products without leaving their homes.
    - Community Engagement: Building a community of dog lovers through social media engagement, fostering a sense of belonging and loyalty.
6. **Channels**:
    
    - E-commerce Website: The primary platform for showcasing products, processing orders, and facilitating transactions.
    - Social Media: Utilizing platforms such as Facebook, Instagram, and Twitter for marketing, customer engagement, and community building.
    - Newsletter: Sending regular updates, promotions, and announcements to subscribers via email.
7. **Customer Relationships**:
    
    - Personalized Support: Offering responsive customer support to address inquiries, provide assistance, and resolve issues promptly.
    - Engagement: Actively engaging with customers through social media interactions, responding to comments, and sharing user-generated content.
8. **Key Activities**:
    
    - Product Sourcing: Identifying and sourcing high-quality dog treats, food, and toys from trusted suppliers and manufacturers.
    - Website Management: Maintaining and updating the e-commerce platform to ensure a seamless shopping experience for customers.
    - Marketing and Promotion: Implementing marketing strategies to attract new customers, retain existing ones, and promote brand awareness.
9. **Key Resources**:
    
    - Product Inventory: Stocking a diverse range of dog treats, food, and toys to meet customer demand.
    - E-commerce Platform: Investing in a robust and user-friendly website for online sales and transactions.
    - Social Media Presence: Building and maintaining an active presence on social media platforms to engage with customers and drive traffic to the website.
10. **Cost Structure**:
    
    - Product Costs: Expenses related to sourcing, purchasing, and stocking inventory.
    - Website Maintenance: Costs associated with hosting, domain registration, website development, and maintenance.
    - Marketing Expenses: Budget allocated for advertising, promotions, and social media marketing campaigns.
11. **Key Partnerships**:
    
    - Suppliers: Establishing partnerships with reliable suppliers and manufacturers to ensure a consistent supply of quality products.
    - Delivery Services: Collaborating with shipping and delivery services to fulfill customer orders efficiently and reliably.
    - Influencers and Affiliates: Partnering with pet influencers or affiliates to promote products and reach a wider audience.
12. **Growth Strategies**:
    
    - Expansion of Product Range: Continuously adding new and innovative products to cater to evolving customer preferences and trends.
    - Geographic Expansion: Scaling operations to reach new geographic markets and expand the customer base.
    - Customer Loyalty Programs: Implementing loyalty programs, discounts, and rewards to incentivize repeat purchases and foster customer loyalty.


# Search Engine Optimization And Social Media Marketing

### Keyword Strategy for Enhanced Online Visibility

In order to optimize the discoverability of my website through search engines, I've developed a comprehensive keyword strategy. This strategy encompasses two main types of keywords:

**Short-Tail (Head Terms) Keywords**: These are concise and broad keywords that capture the essence of my website's offerings in a general sense.

**Long-Tail Keywords**: Long-tail keywords are more specific and detailed phrases that align closely with the products and services offered on my website.

By strategically incorporating both short-tail and long-tail keywords throughout my website's content, I aim to improve its search engine rankings and make it more accessible to users searching for relevant information or products online. This keyword strategy is crucial for enhancing online visibility and attracting targeted traffic to my website.

In my project, I utilized Wordtracker.com to conduct keyword research and identify relevant terms and phrases that align with the content and purpose of my website. By analyzing search trends and user behavior data, I aimed to incorporate these keywords into my titles, descriptions, and content to improve search engine visibility and attract organic traffic. This strategic approach helped me optimize my website's metadata, ensuring that it resonates effectively with search engine algorithms and enhances the discoverability of my content online.

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/wordtracker.png?raw=true" alt="wordtracker">
</div>

### Sitemap Generation with XML-Sitemaps

To streamline the process of creating a sitemap.xml file for my website, I utilized [XML-Sitemaps.](https://www.xml-sitemaps.com/)

By submitting the deployed site URL ([https://fetch-and-feast-4ceb13480b0c.herokuapp.com/](https://fetch-and-feast-4ceb13480b0c.herokuapp.com/)), the tool meticulously crawled through the entire site. Following the completion of this process, it automatically generated a detailed sitemap.xml document. I subsequently downloaded this file and added it into the repository.

### Robots

I've configured the robots.txt file located at the root level of the project. It specifies the default settings, intentionally disallowing access to the admin section, as follows:

```
User-agent: *
Disallow: /admin/
Sitemap: https://fetch-and-feast-4ceb13480b0c.herokuapp.com/sitemap.xml
```

Further links for future implementation:

- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a vibrant social media presence, marked by consistent engagement, can significantly boost sales performance. Leveraging popular platforms like Facebook, known for their extensive user bases, is particularly effective in driving website traffic and expanding brand visibility. Active participation and strategic linking of social media channels to the business site amplify opportunities for sales growth. Moreover, establishing a dedicated Facebook business page further enhances brand credibility and facilitates direct interaction with potential customers.

[Link to Fetch & Feast Facebook Business Page](https://www.facebook.com/profile.php?viewas=100000686899395&id=61556243653249)

<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/facebook.png?raw=true" alt="facebook">
</div>

### Newsletter Marketing

Within my application, I've seamlessly integrated a newsletter sign-up form, providing users with the opportunity to subscribe by submitting their email addresses. This feature aims to cater to users interested in receiving regular updates and promotions.

Furthermore, I've implemented a streamlined unsubscribe process, allowing users to opt-out of the newsletter subscription easily. Upon subscription confirmation, users receive a confirmation email containing a link for unsubscribing, ensuring compliance with email marketing regulations and respecting user preferences.

Looking ahead, I aim to enhance the newsletter marketing strategy by integrating an intuitive frontend management system. This system will facilitate the seamless creation and distribution of newsletters to customers, ensuring an efficient and user-friendly experience for both administrators and subscribers.

# Deployment

The live deployed application can be found deployed on [Heroku](https://fetch-and-feast-4ceb13480b0c.herokuapp.com/).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com/) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: fetch-and-feast).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com/) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected. Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
    
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
    
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
    
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
    
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
    
- From the **Permissions** tab, paste in the following CORS configuration:
    
    ```shell
     [
     	{
     		"AllowedHeaders": [
     			"Authorization"
     		],
     		"AllowedMethods": [
     			"GET"
     		],
     		"AllowedOrigins": [
     			"*"
     		],
     		"ExposeHeaders": []
     	}
     ]
    ```
    
- Copy your **ARN** string.
    
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
    
    - Policy Type: **S3 Bucket Policy**
        
    - Effect: **Allow**
        
    - Principal: `*`
        
    - Actions: **GetObject**
        
    - Amazon Resource Name (ARN): **paste-your-ARN-here**
        
    - Click **Add Statement**
        
    - Click **Generate Policy**
        
    - Copy the entire Policy, and paste it into the **Bucket Policy Editor**
        
        ```shell
         {
         	"Id": "Policy1234567890",
         	"Version": "2012-10-17",
         	"Statement": [
         		{
         			"Sid": "Stmt1234567890",
         			"Action": [
         				"s3:GetObject"
         			],
         			"Effect": "Allow",
         			"Resource": "arn:aws:s3:::your-bucket-name/*"
         			"Principal": "*",
         		}
         	]
         }
        ```
        
    - Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
        
    - Click **Save**.
        
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
    
    - If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management). Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
    - Suggested Name: `group-fetch-and-feast` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
    - Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
        
    - You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.
        
        ```shell
         {
         	"Version": "2012-10-17",
         	"Statement": [
         		{
         			"Effect": "Allow",
         			"Action": "s3:*",
         			"Resource": [
         				"arn:aws:s3:::your-bucket-name",
         				"arn:aws:s3:::your-bucket-name/*"
         			]
         		}
         	]
         }
        ```
        
    - Click **Review Policy**.
        
    - Suggested Name: `policy-fetch-and-feast` (policy + the project name)
        
    - Provide a description:
        
        - "Access to S3 Bucket for fetch-and-feast static files."
    - Click **Create Policy**.
        
- From **User Groups**, click your "group-fetch-and-feast".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-fetch-and-feast") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
    - Suggested Name: `user-fetch-and-feast` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-feast-and-feast`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
    - **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
    - This contains the user's **Access key ID** and **Secret access key**.
    - `AWS_ACCESS_KEY_ID` = **Access key ID**
    - `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com/) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
    - `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
    - `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
    - `https://fetch-and-feast-4ceb13480b0c.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
    - `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com/) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or fetch-and-feast
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com/), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- _replace **app\_name** with the name of your primary Django app name; the folder where settings.py is located_

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace _app\_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
    - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- _repeat this action for each model you wish to backup_

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/leec313/Fetch-and-Feast)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
    - `git clone https://github.com/leec313/Fetch-and-Feast.git` 
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://camo.githubusercontent.com/95fbab4ac41e62a9f66e6d1d78f8249c418b33f8c7739c4f9c593f953f5362de/68747470733a2f2f676974706f642e696f2f627574746f6e2f6f70656e2d696e2d676974706f642e737667)](https://gitpod.io/#https://github.com/leec313/Fetch-and-Feast)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/leec313/Fetch-and-Feast)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

# Credits and Acknowledgements

## Content and Resources

- **Images**: I employed [leonardo.ai](https://app.leonardo.ai/) to generate the majority of product images and a significant portion of blog images. Additionally, I utilized personal photographs as well as images contributed by friends for certain blog posts.

- **Bootstrap Documentation Exploration**: I extensively referred to the Bootstrap documentation to strategize my design approach. The examples provided on getbootstrap.com proved invaluable in understanding how to effectively implement Bootstrap components. [Link to Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    
- **Django Documentation Consultation**: I delved into the Django documentation on multiple occasions, particularly when tackling model implementation and other content-related aspects.
    
- **W3 Schools Reference**: W3 Schools served as a reliable reference throughout the project, offering straightforward CSS examples that were instrumental in various design aspects.
    
- **Code Institute Contribution**:
    
    - The course content for Portfolio Project 5 from Code Institute played a pivotal role in equipping me with the knowledge and skills necessary to complete this project successfully.
    - The structured and comprehensive nature of the course content significantly aided my understanding of project requirements and the Django framework.
    - **Informative and Well-Paced Walkthroughs**:
        - The walkthroughs provided in the course were not only informative but also well-paced, allowing for a step-by-step understanding of concepts and implementation details.
        - The clarity of these walkthroughs facilitated the comprehension of complex topics and reinforced a strong foundation in Django development.
    - **Initial Structure Inspired by CI Walkthrough**:
        - In the project's early stages, I heavily relied on the Code Institute (CI) walkthrough for guidance.
        - The initial project structure drew influence from the CI walkthrough, serving as a scaffold until I acquired a deeper understanding of the Django framework and could confidently make personalized modifications.

## Acknowledgements

I'd like to extend my heartfelt gratitude to the remarkable team at Code Institute, especially my mentor Rory Sheridan and cohort mate Alan Bushell, for their continuous support throughout my final project of the course. Their guidance and encouragement played a pivotal role in helping me overcome challenges and ultimately succeed.

A sincere thank you goes out to all the tutors and fellow students at Code Institute. The collaborative and supportive environment they fostered created an optimal setting for learning. Their shared insights, experiences, and camaraderie greatly enhanced my journey, making it a truly memorable and fulfilling experience.
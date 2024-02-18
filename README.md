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


<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/product-detail.png?raw=true" alt="products">
</div>
<div align="center">
 <img src="https://github.com/leec313/Fetch-and-Feast/blob/main/readme-images/product-detail-mobile.png?raw=true" alt="products-mobile">
</div>
# your User class goes here
class User:
    all_posts = []

    def __init__(self, name, emailAddress, driverLicenceNumber):
        self.name = name
        self.emailAddress = emailAddress
        self.driverLicenceNum = driverLicenceNumber

        # 2. Instance Property: Stores ONLY the posts belonging to this specific user.
        # This is a LIST used for quick lookup of a user's own posts.
        self.user_posts = []

    # 1. Add a method to create a new user post.
    def add_post(self, content):
        """
        Creates a new post and synchronizes it across both the instance list 
        (self.user_posts) and the class list (User.all_posts).
        """
        # Create a dictionary to hold the post data, including the author's name
        # to identify the post in the global list.
        new_post = {
            "author": self.name,
            "content": content,
            # Assign a simple ID based on the current length of the global list.
            "post_id": len(User.all_posts) + 1 
        }
        
        # 4. Sync Step 1: Add the post to the instance list (for quick user access)
        self.user_posts.append(new_post)
        
        # 4. Sync Step 2: Add the post to the class list (the global history)
        User.all_posts.append(new_post)
        
        return new_post
    
    # BONUS: Add a method that allows for deleting a post.
    def delete_post(self, post_id):
        """Deletes a post by ID from both the user's list and the global list."""
        
        # Find the post in the instance list and remove it
        post_to_delete = None
        for i, post in enumerate(self.user_posts):
            if post["post_id"] == post_id:
                post_to_delete = self.user_posts.pop(i)
                break
        
        # 4. Sync Step 3: Remove the post from the global list (only if it was found)
        if post_to_delete:
            try:
                # Find the post in the global list using its reference
                User.all_posts.remove(post_to_delete)
                return f"Post ID {post_id} deleted successfully."
            except ValueError:
                return f"Post ID {post_id} was missing from the global list."
        else:
            return f"Error: Post ID {post_id} not found in {self.name}'s posts."




User_1 = User("John Brown", "jbrown@place.com", "12345")
User_2 = User("Marcy Tree", "mtree@place.com", "12345")

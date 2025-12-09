import os
import time # Import the time module

def delete_translation_files(base_path, valid_langs_str):
    """
    Deletes 'index.<lang_code>.md' files where <lang_code> is not in the
    provided list of valid languages.

    Args:
        base_path (str): The base path of the content directory. Expected
                         structure: <base_path>/<product_folder>/<blog_post_dir>/
        valid_langs_str (str): A pipe-separated string of valid language codes
                                (e.g., "ar|de|es").
    """
    # Convert the pipe-separated string to a set for efficient lookup
    valid_languages = set(valid_langs_str.split('|'))

    print(f"Starting file deletion process in: {base_path}")
    print(f"Valid language codes: {valid_languages}\n")

    deletion_count = 0

    # Walk through the directory tree
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.startswith("index.") and file.endswith(".md"):
                # Extract the language code from the filename
                parts = file.split('.')
                if len(parts) == 3: # Expecting 'index', 'lang_code', 'md'
                    lang_code = parts[1].lower()

                    if lang_code not in valid_languages:
                        file_to_delete = os.path.join(root, file)
                        try:
                            # print(f"  Deleting invalid file: {file_to_delete}")
                            os.remove(file_to_delete)
                            deletion_count += 1 # Increment the counter
                            print(f".{lang_code}", end=' ', flush=True) # Deleting
                        except OSError as e:
                            print(f"  Error deleting {file_to_delete}: {e}")
                    else:
                        print("", end='', flush=True) # Ignoring
                else:
                    print("", end='', flush=True) # Skipping
    
    print(f"\nFiles Deleted: {deletion_count}")
    print(f"----------------------")

# --- Configuration ---
# Your base path
BASE_PATH = "/Users/Work/GitHub/blog.domain-PROD/domain-blog/content/domain/"

# Your list of valid language codes
LANGS_List = "ar|de|es|fa|fr|id|it|ja|ko|pl|pt|ru|th|tr|uk|vi|zh|zh-hant"

# --- Main execution ---
if __name__ == "__main__":
    # --- Dummy Test Environment Setup ---
    # Create some dummy directories and files to test the script
    # This helps you run the script without affecting your actual files initially
    print("--- Setting up dummy test environment ---")
    dummy_base_path = os.path.join(os.getcwd(), "test_content_for_deletion")
    dummy_product_folder = os.path.join(dummy_base_path, "product_A")
    dummy_blog_post_dir_1 = os.path.join(dummy_product_folder, "blog_post_1")
    dummy_blog_post_dir_2 = os.path.join(dummy_product_folder, "blog_post_2")

    os.makedirs(dummy_blog_post_dir_1, exist_ok=True)
    os.makedirs(dummy_blog_post_dir_2, exist_ok=True)

    # Create valid files
    with open(os.path.join(dummy_blog_post_dir_1, "index.ar.md"), "w") as f: f.write("arabic content")
    with open(os.path.join(dummy_blog_post_dir_1, "index.es.md"), "w") as f: f.write("spanish content")
    with open(os.path.join(dummy_blog_post_dir_2, "index.fr.md"), "w") as f: f.write("french content")

    # Create invalid files (these should be deleted)
    with open(os.path.join(dummy_blog_post_dir_1, "index.cs.md"), "w") as f: f.write("czech content (invalid)")
    with open(os.path.join(dummy_blog_post_dir_1, "index.hi.md"), "w") as f: f.write("hindi content (invalid)")
    with open(os.path.join(dummy_blog_post_dir_2, "index.ru.md"), "w") as f: f.write("russian content (valid)")
    with open(os.path.join(dummy_blog_post_dir_2, "index.xx.md"), "w") as f: f.write("unknown content (invalid)")

    # Create other files that should be ignored
    with open(os.path.join(dummy_blog_post_dir_1, "other_file.txt"), "w") as f: f.write("some text")
    with open(os.path.join(dummy_blog_post_dir_1, "image.jpg"), "w") as f: f.write("binary data")
    print("--- Dummy test environment setup complete ---\n")

    print("\n--- Running the file deletion script ---")
    # For actual execution, uncomment the line below and comment out the dummy path
    # delete_invalid_language_files(BASE_PATH, LANGS_List)

    time.sleep(5) # Pause for 5 seconds
    # For testing with the dummy environment:
    delete_translation_files(dummy_base_path, LANGS_List)

    print("\n--- Script finished ---")

    # --- Cleanup Dummy Environment (Optional) ---
    # Uncomment the following lines if you want to remove the dummy files after testing
    # import shutil
    # if os.path.exists(dummy_base_path):
    #     print(f"\nCleaning up dummy directory: {dummy_base_path}")
    #     shutil.rmtree(dummy_base_path)
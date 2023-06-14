# Dorker

Dorker is a command-line tool that allows you to perform Google dork searches easily. It provides a set of predefined dorks for various search scenarios, making it convenient to find specific information on the web.

## Features

- Choose from a list of predefined dork options
- Perform targeted searches by combining search terms with dorks
- Open search results in your default web browser

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/dorker.git
   ```
2. Navigate to the project directory

  ```shell
     cd dorker
  ```
3. Install the required dependencies:

  ```shell
  pip3 install -r requirements.txt
  ```
  
  ##Usage
  
To use Dorker, follow these steps:
  1. Open a terminal or command prompt.
  2. Navigate to the project directory:
   
      ```shell
      cd /path/to/dorker
      ```
3. Run the script with the desired target and dork option:

    ```shell
    python3 dorker.py "your target" <dork_option>
    ```
4. Replace "your target" with the term you want to search for and <dork_option> with the number corresponding to the dork option you want to use.
   Dorker will open your default web browser with the search results.

##Available Dorks 

1. Publicaly Exposed Documents
2. Directory Listing Vulnerability
3. Configuration Files Exposed
4. Database Files Exposed
5. Log Files Exposed
6. Backup & Old Files
7. Login Pages
8. SQL Errors
9. PHP errors
10. PHP info()
11. Search Pasting Sites
12. Search Github & Gitlab
13. Stackoverflow
14. Sign Up Pages
15. Find Subdomains
16. Find Sub - Subdomains

###Example

1. To search for publicaly exposed documents related to "example search", run:

    ```shell
    python3 dorker.py "example search" 1

    ```
  
2. To search for configuration files exposed on the web related to "example search", run:
    ```shell
    python dorker.py "example search" 3
    
    ```

##Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


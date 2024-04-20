## **SEC-0013:** Category testing  

> **Summary:** Verify all inputs can handle Cross-Site Scripting (XSS) attacks.  <br>

**Preconditions:** 
 - Admin or salesperson user must be logged in this session. 

Scenario 1 

 | \# | Step | Expected Behavior | 
 |----|------|-------------------| 
 |  1 | Launch application.                    | Verify that the home screen is shown. | 
 |  2 | In the appbar, tap the hamburger icon. | Verify that the sidebar menu is opened. |  
 |  3 | In the sidebar, tap `Categories` menu item. | Verify that the `Categories` screen is shown. |  
 |  4 | In the appbar, tap `+` icon.           | Verify that the `Create Category` screen is shown. |  
 |  5 | Set the `Category name` textfield to "<script>alert('');<\/script>". | Verify that the `Save` button is enabled. | 
 |  6 | Tap the `Save` button.                              | Verify that the "Input contains invalid characters, please try again." error message is shown. |
 |  7 | Set the `Category name` textfield to "bouquets". | Verify that the `Save` button is enabled. |   
 |  8 | Tap the `Save` button.                              | Verify that the `Loading` screen is shown. |  
 |  9 | Wait until loading is completed.                    | Verify that the `Categories` screen is shown. |  
 | 10 | In the list, find "bouquets" item.       | Verify that the "bouquets" item is visible. | 

**Post-conditions:**  

 - A new category is saved.

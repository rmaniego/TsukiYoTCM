## **USER-0001:** User testing - Add Admin  

> **Summary:** Verify that admin user is saved and displayed successfully.  <br>

**Preconditions:** Admin user must be logged in this session.  

Scenario 1 

 | \# | Step | Expected Behavior | 
 |----|------|-------------------| 
 |  1 | Launch application.                                 | Verify that the home screen is shown. | 
 |  2 | In the appbar, tap the hamburger icon.              | Verify that the sidebar menu is opened. |  
 |  3 | In the sidebar, tap `Users` menu item.              | Verify that the `Users` screen is shown. |  
 |  4 | In the appbar, tap `+` icon.                        | Verify that the `New User` screen is shown. |  
 |  5 | Set the `Name` textfield to "Juan dela Cruz".       | Verify that the `Name` textfield value is "Juan dela Cruz". |  
 |  6 | Set the `Email` textfield to "juandcruz@gmail.com". | Verify that the `Email`textfield value is "juandcruz@gmail.com". |  
 |  7 | Tap the `Next` button.                              | Verify that the `Permission Manager` screen is shown. |  
 |  8 | Enable the `Administrator` toggle button.           | Verify that the `Administrator` toggle button is enabled. |  
 |  9 | Tap the `Next` button.                              | Verify that the `Password` screen is shown. |  
 | 10 | Set the `Password` textfield to "g5#qeL".           | Verify that the `Password`textfield value is "g5#qeL". |
 | 11 | Tap the `Next` button.                              | Verify that the `Loading` screen is shown. |  
 | 12 | Wait until loading is completed.                    | Verify that the `Users` screen is shown. |  
 | 12 | In the list, find "Juan dela Cruz" card item.       | Verify that the "Juan dela Cruz" card item is visible. |

**Post-conditions:**  

 - The user is added to the list of users.

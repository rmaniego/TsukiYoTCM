## **UI-0017:** Product testing  

> **Summary:** Verify that DBCS inputs are saved and displayed properly.  <br>

**Preconditions:**  
 - Admin or salesperson user must be logged in this session. 
 - Categories must not be empty.

Scenario 1 

 | \# | Step | Expected Behavior | 
 |----|------|-------------------| 
 |  1 | Launch application.                    | Verify that the home screen is shown. | 
 |  2 | In the appbar, tap the hamburger icon. | Verify that the sidebar menu is opened. |  
 |  3 | In the sidebar, tap `Products` menu item. | Verify that the `Products` screen is shown. |  
 |  4 | In the appbar, tap `+` icon.           | Verify that the `New` screen is shown. |  
 |  5 |  | Verify that the `Product name` textfield is empty. |   
 |  6 |  | Verify that the `Product price` textfield value is "0.00". |   
 |  7 |  | Verify that the `Reduced price` textfield value is "0.00". |   
 |  8 |  | Verify that the `Category` list item value is "None". |   
 |  9 |  | Verify that the `Description` list item value is empty. |   
 | 10 |  | Verify that the `Bar Code` list item value is empty. |   
 | 11 |  | Verify that the `Unit Cost` list item value is "0.00". |   
 | 12 |  | Verify that the `Unit-of-Measure` list item value is "Unit". |   
 | 13 |  | Verify that the `Add to Catalog` switch is enabled. |   
 | 14 |  | Verify that the `Create product` button is disabled. |   
 | 15 | Set the `Product name` textfield to "宵っ張り Messenger Bag". | Verify that the `Product name` textfield value is "宵っ張り Messenger Bag". |  
 | 16 | Set the `Description` list item to "올빼미 #2093 Men's Single Shoulder Bag Portable Waterproof Small Bags Sports Messenger Bag". | Verify that the `Description` list item value is "올빼미 #2093 Men's Single Shoulder Bag Portable Waterproof Small Bags Sports Messenger Bag". |  
 | 17 | Set the `Category` list item to "Men's Fashion and Accessories". | Verify that the `Category` list item value is "Men's Fashion and Accessories". |  
 | 18 | Set the `Initial stocks on hand` list item to "50". | Verify that the `Initial stocks on hand` list item value is "50". |  
 | 19 | Tap the `Create product` button.             | Verify that the `Loading` screen is shown. |  
 | 20 | Wait until loading is completed.       | Verify that the home screen is shown. |  
 | 21 | Set the `Search` textfield to "Messenger Bag" | Verify that the "Messenger Bag" item is visible. |  

**Post-conditions:**  

 - The product is added to the inventory.
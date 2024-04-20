## **CON-0001:** 2G/3G testing  

> **Summary:** Verify the app is working on 2G/3G network.  <br>

**Preconditions:** 
 - Admin or salesperson user must be logged in this session. 
 - Products and inventory must not be empty, enough for 1 transaction.  
 - All transactions had been cleared or is empty.

Scenario 1 

 | \# | Step | Expected Behavior | 
 |----|------|-------------------| 
 |  1 | Launch application.                    | Verify that the home screen is shown. | 
 |  2 | Tap the first item in the inventory.   | Verify that the default quantity is "1". | 
 |  3 | Tap the `Add to Cart` button.          | Verify that the item count increments by "1". | 
 |  4 | Tap the `Go to Cart` button.           | Verify that the total item count is "1". | 
 |  5 | Tap the `Checkout` button.             | Verify that `Payment Methods` option is highlighted.  
 |  6 | Tap the `Next` button.                 | Verify that the `Cash Payment` screen is shown. | 
 |  7 | Tap the `Charge` button.               | Verify the `Done` screen is shown. | 
 |  8 | Tap the `New Sale` button.             | Verify that the `Loading` screen is shown. |  
 |  9 | Wait until loading is completed.       | Verify that the home screen is shown. |  
 | 10 | In the appbar, tap the hamburger icon. | Verify that the sidebar menu is opened. |   
 | 11 | In the sidebar, tap `Transactions` menu item. | Verify that the `Transactions` screen is shown. |   
 | 12 | Check the number of daily sales. | Verify that the daily sale(s) is "1". |   

**Post-conditions:**  

 - The transcation is recorded.
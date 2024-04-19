## **PERF-0015:** Doze-mode testing  

> **Summary:** Verify that the app can handle POS operations after timeouts.  <br>

**Preconditions:** 
 - Admin or salesperson user must be logged in this session. 
 - Products and inventory must not be empty, enough for 1 transaction.  
 - All transactions had been cleared or is empty.

Scenario 1 

 | \# | Step | Expected Behavior | 
 |----|------|-------------------| 
 |  1 | Launch application.                    | Verify that the home screen is shown. | 
 |  2 | Tap the first item in the inventory.   | Verify that the default quantity is "1". | 
 |  3 | Wait for 15s until screen timeouts     | Verify the device entered sleep state. | 
 |  4 | Unlock device.                         | Verify that the `Item Quantity` screen is shown. | 
 |  5 | Tap the `Add to Cart` button.          | Verify that the item count increments by "1". | 
 |  6 | Wait for 15s until screen timeouts     | Verify the device entered sleep state. | 
 |  7 | Unlock device.                         | Verify that the `Item Quantity` screen is shown. | 
 |  8 | Tap the `Go to Cart` button.           | Verify that the total item count is "1". | 
 |  9 | Wait for 15s until screen timeouts     | Verify the device entered sleep state. | 
 | 10 | Unlock device.                         | Verify that the `Cart` screen is shown. | 
 | 11 | Tap the `Checkout` button.             | Verify that `Payment Methods` option is highlighted.  | 
 | 12 | Wait for 15s until screen timeouts     | Verify the device entered sleep state. | 
 | 13 | Unlock device.                         | Verify that the `Payment Methods` screen is shown. | 
 | 14 | Tap the `Next` button.                 | Verify that the `Cash Payment` screen is shown. | 
 | 15 | Wait for 15s until screen timeouts     | Verify the device entered sleep state. | 
 | 16 | Unlock device.                         | Verify that the `Cash Payment` screen is shown. | 
 | 17 | Tap the `Charge` button.               | Verify the `Done` screen is shown. | 
 | 18 | Wait for 15s until screen timeouts     | Verify the device entered sleep state. | 
 | 19 | Unlock device.                         | Verify that the `Done` screen is shown. | 
 | 20 | Tap the `New Sale` button.             | Verify that the `Loading` screen is shown. |  
 | 21 | Wait until loading is completed.       | Verify that the home screen is shown. |    
 | 22 | In the appbar, tap the hamburger icon. | Verify that the sidebar menu is opened. |   
 | 23 | In the sidebar, tap `Transactions` menu item. | Verify that the `Transactions` screen is shown. |   
 | 24 | Check the number of daily sales. | Verify that the daily sale(s) is "1". |   

**Post-conditions:**  

 - The transcation is recorded.

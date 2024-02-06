// Function to retrieve the current URL of the active tab
function getCurrentTabUrl(callback) {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      var url = tabs[0].url;
      callback(url);
    });
  }
  
  // Example: Call the function to get the URL and log it
  getCurrentTabUrl(function(url) {
    console.log("Current URL:", url);
    // Now you can send 'url' to your server or perform any other action
  });
  
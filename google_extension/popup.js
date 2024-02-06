function updateTargetUrl() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var url = tabs[0].url;
    document.getElementById('target_url').textContent = url; // Update <p> content
  });
}

function sendUrlAndOptionsToServer(url, selectedOptions) {
  const data = {
    url: url,
    selectedOptions: selectedOptions
  };

  fetch('http://localhost:5000/execute-script', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data), // Send URL and options to the server
  })
  .then(response => {
    // Handle the response if needed
  })
  .catch(error => {
    // Handle errors if the request fails
  });
}


document.addEventListener('DOMContentLoaded', function() {
  updateTargetUrl();
  document.getElementById('startButton').addEventListener('click', function() {
    // Get the current URL from the content script
    
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      var url = tabs[0].url;
      var checkboxes = document.querySelectorAll('input[name="fields"]:checked');
      var selectedOptions = Array.from(checkboxes).map(checkbox => checkbox.value);
      sendUrlAndOptionsToServer(url, selectedOptions);
    });
    

    // Send data to Flask server
    
  });

  // ... (other code)
});

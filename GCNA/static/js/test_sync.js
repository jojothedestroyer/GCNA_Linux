



document.getElementById('activateButton').addEventListener('click', function () {
  activateCode();
});




function activateCode() {

var additionalEndpoints = [
    'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'Worker', 'Farmer','visit' ,'In-House-Drying',
    'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary',
    'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur',
    'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees',
    'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition',
    'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality',
    'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy'
];
// Open IndexedDB
var openRequest = indexedDB.open('GCNA', 2);

openRequest.onsuccess = function (e) {
  var db = e.target.result;

  additionalEndpoints.forEach(function (endpoint) {
    var transaction = db.transaction([endpoint]);
    var objectStore = transaction.objectStore(endpoint);
    var getRequest = objectStore.getAll();

    getRequest.onsuccess = function (event) {
      var results = event.target.result;
      results.forEach(function (result) {
        fetch(`/api/${endpoint}2/${result.id}/`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
          },
        })
          .then((response) => {
            if (response.status === 404) {
              // Object does not exist in Django, make a POST request to create it
              return fetch(`/api/${endpoint}/`, {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify(result),
              });
            } else if (response.status === 200) {
              // Object exists in Django, check if ID matches
              return response.json().then((data) => {
                if (data.id !== result.id) {
                  // If the IDs don't match, delete the entry from Django
                  return fetch(`/api/${endpoint}2/${result.id}/`, {
                    method: 'DELETE',
                    headers: {
                      'X-CSRFToken': getCookie('csrftoken'),
                    },
                  })
                    .then((deleteResponse) => {
                      if (deleteResponse.status === 204) {
                        console.log(`Deletion successful for ${endpoint}: ID ${result.id}`);
                      } else {
                        console.error(`Deletion failed for ${endpoint}: ID ${result.id}`);
                      }
                      // Continue with the rest of the code
                      return fetch(`/api/${endpoint}/`, {
                        method: 'POST',
                        headers: {
                          'Content-Type': 'application/json',
                          'X-CSRFToken': getCookie('csrftoken'),
                        },
                        body: JSON.stringify(result),
                      });
                    });
                } else {
                  // Object exists and IDs match, make a PATCH request to update it
                  return fetch(`/api/${endpoint}2/${result.id}/`, {
                    method: 'PATCH',
                    headers: {
                      'Content-Type': 'application/json',
                      'X-CSRFToken': getCookie('csrftoken'),
                    },
                    body: JSON.stringify(result),
                  });
                }
              });
            } else {
              return Promise.reject('Unknown error');
            }
          })
          .then((response) => response.json())
          .then((data) => {
            console.log(`Success for ${endpoint}:`, data);
          })
          .catch((error) => {
            console.error(`Error for ${endpoint}:`, error);
          });
      });
    };
  });
};




function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


}
























































// var openRequest = indexedDB.open('GCNA', 2);

// openRequest.onsuccess = function(e) {
//     var db = e.target.result;
//     var transaction = db.transaction(["visit"]);
//     var objectStore = transaction.objectStore("visit");
//     var getRequest = objectStore.getAll();

//     getRequest.onsuccess = function(event) {
//         var results = event.target.result;
//         results.forEach(function(result) {
//             fetch('/api/visit/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCookie('csrftoken')

//                 },
//                 body: JSON.stringify(result),
//             })
//             .then(response => response.json())
//             .then(data => console.log('Success:', data))
//             .catch((error) => console.error('Error:', error));
//         });
//     };
// };



// openRequest.onsuccess = function(e) {
//     var db = e.target.result;
//     var transaction = db.transaction(["visit"]);
//     var objectStore = transaction.objectStore("visit");
//     var getRequest = objectStore.getAll();

//     getRequest.onsuccess = function(event) {
//         var results = event.target.result;
//         results.forEach(function(result) {
//             fetch('/api/visit2/'+ result.id + '/', {
//                 method: 'PATCH',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCookie('csrftoken')

//                 },
//                 body: JSON.stringify(result),
//             })
//             .then(response => response.json())
//             .then(data => console.log('Success:', data))
//             .catch((error) => console.error('Error:', error));
//         });
//     };
// };




// openRequest.onsuccess = function(e) {
//     var db = e.target.result;
//     var transaction = db.transaction(["visit"]);
//     var objectStore = transaction.objectStore("visit");
//     var getRequest = objectStore.getAll();

//     getRequest.onsuccess = function(event) {
//         var results = event.target.result;
//         results.forEach(function(result) {
//             fetch('/api/visit2/' + result.id + '/', {
//                 method: 'GET',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCookie('csrftoken')
//                 },
//             })
//             .then(response => {
//                 if (response.status === 404) {
//                     // Object does not exist in Django, make a POST request to create it
//                     return fetch('/api/visit/', {
//                         method: 'POST',
//                         headers: {
//                             'Content-Type': 'application/json',
//                             'X-CSRFToken': getCookie('csrftoken')
//                         },
//                         body: JSON.stringify(result),
//                     });
//                 } else {
//                     // Object exists in Django, make a PATCH request to update it
//                     return fetch('/api/visit2/' + result.id + '/', {
//                         method: 'PATCH',
//                         headers: {
//                             'Content-Type': 'application/json',
//                             'X-CSRFToken': getCookie('csrftoken')
//                         },
//                         body: JSON.stringify(result),
//                     });
//                 }
//             })
//             .then(response => response.json())
//             .then(data => console.log('Success:', data))
//             .catch((error) => console.error('Error:', error));
//         });
//     };
// };




// openRequest.onsuccess = function(e) {
//     var db = e.target.result;
//     var transaction = db.transaction(["DriedA"]);
//     var objectStore = transaction.objectStore("DriedA");
//     var getRequest = objectStore.getAll();

//     getRequest.onsuccess = function(event) {
//         var results = event.target.result;
//         results.forEach(function(result) {
//             fetch('/api/DriedA2/' + result.id + '/', {
//                 method: 'GET',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCookie('csrftoken')
//                 },
//             })
//             .then(response => {
//                 if (response.status === 404) {
//                     // Object does not exist in Django, make a POST request to create it
//                     return fetch('/api/DriedA/', {
//                         method: 'POST',
//                         headers: {
//                             'Content-Type': 'application/json',
//                             'X-CSRFToken': getCookie('csrftoken')
//                         },
//                         body: JSON.stringify(result),
//                     });
//                 } else {
//                     // Object exists in Django, make a PATCH request to update it
//                     return fetch('/api/DriedA2/' + result.id + '/', {
//                         method: 'PATCH',
//                         headers: {
//                             'Content-Type': 'application/json',
//                             'X-CSRFToken': getCookie('csrftoken')
//                         },
//                         body: JSON.stringify(result),
//                     });
//                 }
//             })
//             .then(response => response.json())
//             .then(data => console.log('Success:', data))
//             .catch((error) => console.error('Error:', error));
//         });
//     };
// };



// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         let cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             let cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

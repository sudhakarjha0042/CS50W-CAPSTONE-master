const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function Play() {
  document.querySelectorAll('.card').forEach(card => card.remove());
  const container = document.createElement('div');
  var html = `
    <form>
      <div class="card text-center justify-content-center bg-dark text-white mt-5" style="margin: auto;position: relative;border: 1px dashed #fff;">
        <div class="card-body">
          <div class="form-group">
            <label for="formGroupExampleInput">Example label</label>
            <input type="text" class="form-control my-2" id="formGroupExampleInput" placeholder="Example input">
            <select class="form-select" name="Choose Language">
            <option selected>Choose Language</option>
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="mr">Marathi</option>
            <option value="es">Spanish</option>
            <option value="fr">French</option>
            <option value="de">German</option>
            <option value="it">Italian</option>
            <option value="ja">Japanese</option>
            <option value="ko">Korean</option>
            <option value="pt">Portuguese</option>
            <option value="ru">Russian</option>
            <option value="zh">Chinese</option>
          </select>
          <select class="form-select my-1" name="Additional Feature">
            <option selected>Additional Feature</option>
            <option value="ReadFull">Listen Full Article</option>
            <option value="Summarize">summarized</option> 
          </select>
            <button type="submit" class="btn btn-Primary my-1" onclick="fetchsummary()">Submit</button>
        </div>
      </div>
    </form>
  `;
  container.innerHTML = html;
  document.body.appendChild(container);
}

function fetchsummary() {
  event.preventDefault();
  const loadingDiv = document.createElement('div');
  loadingDiv.setAttribute('id', 'loading');
  const timerElement = document.createElement('p');
  let timeLimit=60;
  var interval = setInterval(function() {
    timeLimit--;
    if (timeLimit == 0) {
      clearInterval(interval);
      timerElement.innerHTML = "We're sorry, but there seems to be an issue with the news server at the moment. Please try selecting a different news source or category to continue browsing the latest news. If you continue to experience issues, please contact our support team for further assistance.";
    } else {
      timerElement.innerHTML = 'Loading Please Wait... (' + timeLimit + ' Max seconds remaining)';
    }
  }, 1000);
  loadingDiv.appendChild(timerElement);
  document.body.appendChild(loadingDiv);
  const input = document.getElementById("formGroupExampleInput").value;
  let selectedLanguage = "";
  let selectedFeature = "";
  const featureSelect = document.querySelector('select[name="Additional Feature"]');
  selectedFeature = featureSelect.value;
  const languageSelect = document.querySelector('select[name="Choose Language"]');
  selectedLanguage = languageSelect.value;
  fetch(`getSummary/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify({
        selectedLanguage: selectedLanguage,
        selectedFeature: selectedFeature,
      input: input
    })
  })
  .then(response => response.json())
  .then(data => {
      const container = document.createElement('div');
      var html = `
        <div class="card text-center justify-content-center bg-dark text-white mt-5" style="margin: auto;position: relative;border: 1px dashed #fff;">
          <div class="card-body">
            <p class="card-text">${data['summary']}</p>
            <div class="summary-container m-2"></div>
            <div class="audio">
            <audio id="audio_player" controls>
            <source id="audio_source" src="${data['audio_file']}" type="audio/mpeg">
            Your browser does not support the audio element.
          </audio>
          </div>
          </div>
        </div>
      `;
      container.innerHTML = html;
      document.body.appendChild(container);
    document.querySelector('#loading').remove();
  })
  .catch(error => console.error(error));

}

  
function fetchNews(input, forwhat) {
event.preventDefault(); // prevent the form from submitting
var timeLimit = 50;
const loadingDiv = document.createElement('div');
loadingDiv.setAttribute('id', 'loading');
const timerElement = document.createElement('p');
var interval = setInterval(function() {
  timeLimit--;
  if (timeLimit == 0) {
    clearInterval(interval);
    timerElement.innerHTML = "We're sorry, but there seems to be an issue with the news server at the moment. Please try selecting a different news source or category to continue browsing the latest news. If you continue to experience issues, please contact our support team for further assistance.";
  } else {
    timerElement.innerHTML = 'Loading Please Wait... (' + timeLimit + ' Max seconds remaining)';
  }
}, 1000);
loadingDiv.appendChild(timerElement);
document.body.appendChild(loadingDiv);
  document.querySelectorAll('.card').forEach(card => card.remove());

  fetch(`/${forwhat}/${input}`)
    .then(response => response.json())
    .then(data => {

      document.querySelector('#loading').style.display = 'none';
      let summaries = data;
      for (let summary of summaries) {
        const container = document.createElement('div');
        let link = summary.link;
        var html = `
          <div class="card text-center justify-content-center bg-dark text-white mt-5" style="margin: auto;position: relative;border: 1px dashed #fff;">
            <img class="card-img-top" src="${summary.image}" onerror="this.src='/static/images/dark final logo.png'" style="height: 55vh;">
            <div class="card-body">
              <h5 class="card-title">${summary.title}</h5>
              <p class="card-text">${summary.summary}</p>
              <a href="${summary.link}" class="btn btn-primary bg-light text-dark">Details</a>
              <select class="form-select" name="Choose Language">
              <option selected>Choose Language</option>
              <option value="en">English</option>
              <option value="hi">Hindi</option>
              <option value="mr">Marathi</option>
              <option value="es">Spanish</option>
              <option value="fr">French</option>
              <option value="de">German</option>
              <option value="it">Italian</option>
              <option value="ja">Japanese</option>
              <option value="ko">Korean</option>
              <option value="pt">Portuguese</option>
              <option value="ru">Russian</option>
              <option value="zh">Chinese</option>
            </select>
            
              <select class="form-select" name="Additional Feature">
                <option selected>Additional Feature</option>
                <option value="ReadFull">Listen Full Article</option>
                <option value="Summarize">summarized</option> 
              </select>
              <div class="summary-container m-2"></div>
              <div class="audio"></div>
            </div>
          </div>
        `;
        container.innerHTML = html;
        document.body.appendChild(container);
        
        const featureSelect = container.querySelector('select[name="Additional Feature"]');
        featureSelect.addEventListener("change", function() {
          const selectedFeature = this.value;
          const languageSelect = container.querySelector('select[name="Choose Language"]');
          const selectedLanguage = languageSelect.value;
          if (selectedFeature === "Summerize") {
            callviews(selectedLanguage, selectedFeature, link, container);
          }else{
            callviews(selectedLanguage, selectedFeature, link, container);
          }
        });
      }

      document.querySelector('#loading').remove();
    })
    .catch(error => console.error(error));

}

function callviews(selectedLanguage, selectedFeature, link, container) {
if (selectedLanguage === "Choose Language") {
  selectedLanguage = "en";
}


var timeLimit = selectedFeature === "ReadFull" ? 70 : 50;


var summaryContainer = container.querySelector('.summary-container');
var audioContainer = container.querySelector('.audio');

summaryContainer.innerHTML = 'Loading please wait... (' + timeLimit + ' seconds remaining)';

var interval = setInterval(function() {
  timeLimit--;
  if (timeLimit == 0) {
    clearInterval(interval);
    summaryContainer.innerHTML = "Sorry, the summary could not be loaded.";
  } else {
    summaryContainer.innerHTML = 'Loading please wait... (' + timeLimit + ' Max seconds remaining)';
  }
}, 1000);

if (selectedFeature == "Summarize") {
  fetch('summerize/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
      selectedLanguage: selectedLanguage,
      link: link
    })
  })
  .then(response => response.json())
  .then(data => {
    if (summaryContainer) {
      summaryContainer.innerHTML = "<b>Summary: </b>"+data['summary'];

      var html = `
        <audio id="audio_player" controls>
          <source id="audio_source" src="${data['audio_file']}" type="audio/mpeg">
          Your browser does not support the audio element.
        </audio>`;
      audioContainer.innerHTML = html;
    } else {
      console.error("Could not find the specified container with id: " + container);
    }
    clearInterval(interval); 
  })
  .catch(error => {
    console.error("An error occurred while fetching the data: " + error);
    clearInterval(interval);
  });
}
else if (selectedFeature == "ReadFull") {
  fetch('ReadFull/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
      selectedLanguage: selectedLanguage,
      link: link
    })
  })
  .then(response => response.json())
  .then(data => {
    if (audioContainer) {
      var html = `
        <audio id="audio_player" controls>
          <source id="audio_source" src="${data['audio_file']}" type="audio/mpeg">
          Your browser does not support the audio element.
        </audio>`;
      summaryContainer.innerHTML = "";  
      audioContainer.innerHTML = html;
    } else {
      console.error("Could not find the specified container with id: " + container);
    }
    clearInterval(interval);
  })
  .catch(error => {
    console.error("An error occurred while fetching the data: " + error);
    clearInterval(interval);
  });
}
}

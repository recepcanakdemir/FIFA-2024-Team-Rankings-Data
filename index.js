fetch('teams_data.json')
.then(response => response.json())
.then(data => {
    // Handle the data fetched from the JSON file
    console.log(data);
    addTeamItem(data)
    
  })
  .catch(error => {
    console.error('Error fetching the JSON file:', error);
  });


const addTeamItem = data => {
  data.forEach( e => {
    if(e.Name != undefined){
      let league = e.League;
      let name = e.Name;
      let image = e.image;
      let stars = e.stars;
      let teamRatings = e.team_Ratings;
      let ATT = teamRatings.ATT;
      let DEF = teamRatings.DEF;
      let MID = teamRatings.MID;
      let OVR = teamRatings.OVR;

      let card = document.createElement('div');
      card.innerHTML = `
      <div class="card" style="width: 18rem;">
      <img class="card-img-top" src="${image}" alt="Card image cap">
      <div class="card-body">
          <h5 class="card-title">${name}</h5>
          <p class="card-text">League: ${league}</p>
          <p class="card-text">Stars: ${stars}</p>
          <p class="card-text">Team Ratings</p>
          <div class="d-flex flex-column">
              <div class="d-flex justify-content-between">
                  <p class="card-text">ATT: ${ATT}</p>
                  <p class="card-text">DEF: ${DEF}</p>
              </div>
              <div class="d-flex justify-content-between">
                  <p class="card-text">MID: ${MID}</p>
                  <p class="card-text">OVR: ${OVR}</p>
              </div>
          </div>
          <!-- Add other properties as needed -->
          <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
    `;


    document.querySelector('.container').appendChild(card);
    }
 });
}
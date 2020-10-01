const initialState = {
  hidden_companies: []
};
function rootReducer(state = initialState, action) {
  let hidden_companies =
    localStorage.getItem('hidden_companies') ?
      JSON.parse(localStorage.getItem('hidden_companies')) : []
  if (action.type === "HIDE_COMPANY") {
    if (hidden_companies.indexOf(action.payload) === -1) {
      hidden_companies.push(action.payload)      
    }
  }
  else if (action.type === "SHOW_COMPANY") {
    if (hidden_companies.filter(c=> c.id === action.payload.id).length > 0) {
      hidden_companies = hidden_companies.filter(c => c.id !== action.payload.id)
    }
  }
  localStorage.clear()
  localStorage.setItem('hidden_companies', JSON.stringify(hidden_companies))
  return Object.assign({}, state, {
    hidden_companies: hidden_companies
  });
};

export default rootReducer;

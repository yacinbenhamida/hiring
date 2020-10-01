const initialState = {
    hidden_companies: []
  };
  
  function rootReducer(state = initialState, action) {
    if (action.type === "HIDE_COMPANY") {   
        return Object.assign({}, state, {
          hidden_companies : state.hidden_companies.concat(action.payload)
        });
      }
      else if(action.type === "SHOW_COMPANY"){
        return Object.assign({}, state, {
          hidden_companies : state.hidden_companies.filter(c=>c.id!==action.payload.id)
          });
      }
      localStorage.clear()
      localStorage.setItem('hidden_companies',state.hidden_companies)
    return state;
  };
  
  export default rootReducer;
  
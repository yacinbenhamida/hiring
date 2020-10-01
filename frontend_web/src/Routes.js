import React from 'react'
import {
    Switch,
    Route, BrowserRouter as Router,
    Redirect ,
} from "react-router-dom";
import Companies from './Companies'
import CompanyDetails from './CompanyDetails';
export default function Routes() {
    return (
        <Router>
            <Switch>
                <Route
                exact
                    path="/api/companies/:id"
                   >
                   <CompanyDetails />
                   </Route>
                <Route
                exact
                    path="/api/companies/"                   
                >
                <Companies/></Route>
                <Redirect from="/" to="/api/companies/" />
            </Switch>
        </Router>)
}

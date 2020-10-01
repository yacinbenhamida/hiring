import React, { Component } from 'react'
import CompaniesList from './CompaniesList'
import Axios from 'axios'
import LinearProgress from '@material-ui/core/LinearProgress';
import {containerStyles} from './style'
import { hideCompany,showCompany } from "./store/actions/index";
import store from './store';
window.store = store;
window.hideCompany = hideCompany;
export default class Companies extends Component {
    state = {
        companies : [],
        totalRecords : 0,
        currentPage : 0,
        hidden_companies : []
    }
    componentDidMount(){
        console.log(localStorage.getItem('hidden_companies'));
        if(localStorage.getItem('hidden_companies')){
            this.setState({hidden_companies : localStorage.getItem('hidden_companies') ? JSON.parse(localStorage.getItem('hidden_companies')) : []})
        }
        this.fetchData(1)
    }
    fetchData = async (page) => {
        await Axios.get("http://localhost:8000/companies/?format=json&page="+page)
        .then(res => {
            let finalTab = []
            if(this.state.hidden_companies){
                this.state.hidden_companies.forEach(elem=>{
                    finalTab = res.data.results.filter(c=>c.id!==elem)
                })
                this.setState({companies : finalTab,totalRecords : res.data.count})
            } 
            else this.setState({companies : res.data.results,totalRecords : res.data.count})
        }) 
    }
    pageChangeHandle = (page) => {
            if(page === 1){
                this.fetchData(2)
                this.setState({currentPage : 1})
            }             
            else {
                this.setState({currentPage : page},()=>{
                    this.fetchData(page > 0 ? page : 1)
                })               
            }
    }
    redirect = (company) => {
        console.log(company)
        console.log(this.props)
        window.location.href = "/api/companies/"+company.id
    }
    handleSetHiddenCompanys = (selectedItems) => {
        console.log(selectedItems)
        selectedItems.forEach(item=>{
            this.setState({companies : this.state.companies.filter(c=>c.id !== item)})
        })
        console.log(this.state.companies)
    }
    render() {
        if(this.state.companies && this.state.companies.length > 0){
            return (
                <div>
                    <CompaniesList 
                    totalRecords={this.state.totalRecords} 
                    selectedPage={(e)=>this.pageChangeHandle(e)} 
                    companies={this.state.companies}
                    keyPage={this.state.currentPage}
                    companyForDetails={this.redirect}
                    companysTobeHidden={this.handleSetHiddenCompanys}
                    />
                </div>
            )
        }
        else {
            return (
                <div className={containerStyles.root}>
                    <LinearProgress />
                </div>
            )
        }
    }
}

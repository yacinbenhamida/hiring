import React, { Component } from 'react'
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import {cardStyle} from './style'
import { withRouter } from "react-router";
import Axios from 'axios';
import { LinearProgress } from '@material-ui/core';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Switch from '@material-ui/core/Switch';
import { hideCompany,showCompany } from "./store/actions/index";
import store from './store';
window.store = store;
window.hideCompany = hideCompany;
window.showCompany = showCompany
class CompanyDetails extends Component {
    state = {
        company : null,
        isHidden : false,
    }
    componentDidMount(){
        const id = this.props.match.params.id;
        if(id){
            this.fetchData(id)          
        }       
    }
    loadCurrentCompanyState = (id)=>{
        let hidden_companies = localStorage.getItem('hidden_companies') ? JSON.parse(localStorage.getItem('hidden_companies')) : []
        if(hidden_companies.filter(h=>h.id===this.state.company.id).length > 0) 
                    this.setState({isHidden : true})
    }
    fetchData = async (id) => {
        await Axios.get("http://localhost:8000/companies/"+id)
        .then(res => { 
            this.setState({company : res.data})
            this.loadCurrentCompanyState(id)
        }) 
    }
    hideShowCompany = ()=>{
        if(this.state.isHidden){
            store.dispatch(showCompany({ id: this.state.company.id }) );
        }
        else{
            store.dispatch(hideCompany({ id: this.state.company.id }) );
        }
        this.setState({isHidden : !this.state.isHidden})
    }
    render() {
        const classes = cardStyle
        if(this.state.company){
        return (
            <Card className={classes.root}>
              <CardContent>
                <Typography className={classes.title} color="textSecondary" gutterBottom>
                 Details of
                </Typography>
                <Typography variant="h5" component="h2">
                   {this.state.company.name}
                </Typography>
                <Typography className={classes.pos} color="textSecondary">
                  source : {this.state.company.source_name} 
                </Typography>
                <Typography variant="body2" component="p">
                 Address : {this.state.company.address} {this.state.company.postal_code} {this.state.company.city} <br/> {this.state.company.country}
                </Typography>
                <FormControlLabel
                    control={
                        <Switch
                            checked={this.state.isHidden}
                            onChange={this.hideShowCompany}
                            name="hidden"
                            color="primary"
                  />
                }
                label={this.state.isHidden ? 'Hidden' : 'Visible'}
              />
              </CardContent>
             
              <CardActions>
                <Button size="small">Contact</Button>
                <Button size="small">{this.state.company.phone}</Button>
                <Button size="small">{this.state.company.email}</Button>
              </CardActions>
            </Card>
          );
        }
        else{
            return (
                <div>
                    <LinearProgress />
                </div>
            )
        }
    }
}
export default withRouter(CompanyDetails)
import React, { Component } from 'react'
import { useParams } from 'react-router-dom';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import {cardStyle} from './style'
import { withRouter } from "react-router";
import Axios from 'axios';
import { LinearProgress } from '@material-ui/core';
class CompanyDetails extends Component {
    state = {
        company : null
    }
    componentDidMount(){
        const id = this.props.match.params.id;
        if(id){
            this.fetchData(id)
        }
        
    }
    fetchData = async (id) => {
        await Axios.get("http://localhost:8000/companies/"+id)
        .then(res => { console.log(res)
            this.setState({company : res.data})
        }) 
    }
    render() {
        //let { id } = this.useParams();
        const classes = cardStyle
        const bull = <span className={classes.bullet}>•</span>;
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
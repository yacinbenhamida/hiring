import React from 'react';
import './App.css';
import clsx from 'clsx';
import Routes from './Routes';
import {styles} from './style'
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import { Typography } from '@material-ui/core';
import CompanyDetails from './CompanyDetails';
import store from "./store/index";
import { hideCompany,showCompany } from "./store/actions/index";
const useStyles = styles
window.store = store;
window.hideCompany = hideCompany;
window.showCompany = showCompany
function App() {
  const classes = useStyles();
  return (
    <>
      <div className={classes.root}>
      <CssBaseline />
      <AppBar position="absolute" className={clsx(classes.appBar,classes.appBarShift)}>
        <Toolbar className={classes.toolbar}>
          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
            Companies
          </Typography>
        </Toolbar>
      </AppBar>
      <main className={classes.content}>
        <div className={classes.appBarSpacer} />
        <Container maxWidth="lg" className={classes.container}>
          <Grid container spacing={3}>
            <Grid item xs={12}>
              <Paper>
              <Routes />
              </Paper>
            </Grid>
          </Grid>
        </Container>
      </main>
    </div>
    </>
  );
}

export default App;

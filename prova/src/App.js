
import './App.css';

import Map from "./component/Map";
import Header from "./component/Header";
import OutputForm from "./component/OutputForm";
import InputForm from "./component/InputForm";
import CardBase from "./component/CardBase";

import {React,useState} from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import { Card } from 'react-bootstrap';
import Navbar from "react-bootstrap/Navbar";
import styled,{css} from 'styled-components';


function App() {

  const [region,setRegion] = useState("");
  const [style,setStyle] = useState("");

  function getRegion(){
    return region;
  };  
  function getStyle(){
    return style;
  }

    

  const mapBody = <Map callbackRegion={setRegion}/>;
  const inputBody = <InputForm setStyle={setStyle} />;
  const outputBody = <OutputForm getStyle={getStyle} getRegion={getRegion} />;
  
  const Navbar1 = styled(Navbar)`
  background-color: #8A9899 !important; 
  border: 4px solid;
  border-color: #F9966E;
  border-radius: 6px !important;
  text-align: center !important;
    `;
  
    
  return (
    <div>
    <Container style={{border:"1 px"}}>
    
          <Header/>
          <Row >
          <Col><CardBase header={"Choose Style"} body={inputBody} /></Col>
          <Col><CardBase header={"Choose Region"} body={mapBody} /></Col>
    
          </Row>
          <Navbar1/>
          <Row><Col><CardBase header={"Output"} body={outputBody}/></Col></Row>
         
    </Container>
             
    
    
    </div>
);
}

export default App;

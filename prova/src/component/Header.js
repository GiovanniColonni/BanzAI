import React from 'react';

import Navbar from "react-bootstrap/Navbar";
import Image from "react-bootstrap/Image";
import {Row,Col,Container} from "react-bootstrap";

import styled,{css} from 'styled-components';

import logo from "./logo.png"
function Header(){

    
    const Navbar1 = styled(Navbar)`
    background-color: #8d9db6 !important; 
    border-color: #F9966E
    border-width: 2px;
    `;

    return(
        <Navbar1 id={"head"} expand="lg">
            <Container>
            <Row ls={0}><Col></Col><Col><h1>BanzAI</h1></Col><Col></Col></Row>
            <Row><h5>Catch the trend</h5></Row>
            <Image src={logo} rounded/>    
            </Container>
        </Navbar1>
    );

};

export default Header;
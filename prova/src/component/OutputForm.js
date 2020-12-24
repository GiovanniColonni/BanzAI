import {Container,Row,Col} from "react-bootstrap";

function OutputForm({getRegion,getStyle}){
    
    return(
        <Container>

            <Row><h1>Out</h1></Row>
            <Row>
            <p>Selected : </p>
            <pre>{"\n"+getRegion()}</pre>
            <pre>{"\n  "+getStyle()}</pre>
            </Row>
    

        </Container>
        
     
        
    );
};

export default OutputForm

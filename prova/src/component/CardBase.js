
import Card from "react-bootstrap/Card"
import styled,{css} from 'styled-components';

function CardBase({header,body}){

    const CardB = styled(Card)`
    margin: 1rem auto;
    border: 1rem auto;
    border-color: #F9966E;
    
    `;

    return(
        <CardB>
            <Card.Header as={"h5"}>{header}</Card.Header>
            <Card.Body>{body}</Card.Body>
        </CardB>
    );

};

export default CardBase;

import Form from "react-bootstrap/Form";
import styled,{css} from 'styled-components'

function InputForm({setStyle}){


    // per cambiare colori della card https://styled-components.com/docs/basics#styling-any-components
    return(
        

                <Form.Control as="select" onChange={(event)=>{setStyle(event.target.value)}}>
                    <option>Casual</option>
                    <option>Sports</option>
                    <option>Classic</option>
                    <option>Exotic</option>
                    <option>Street</option>
                    <option>Vintage</option>
                    <option>Rocker</option>
                    <option>Boho</option>
                </Form.Control>
            
        
    );
};

export default InputForm;
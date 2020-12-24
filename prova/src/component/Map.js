import {createRef, React,useState,useRef,useEffect} from "react"
import { VectorMap } from '@south-paw/react-vector-maps';
import styled,{css} from 'styled-components'
import ReacDOM from "react-dom";


//import 'react-calendar/dist/Calendar.css';

import italy from './italy.json'

const Map = ({callbackRegion}) =>{
   const [region, setRegion] = useState("");
    const S = styled.div`
         
    margin: 1rem auto;
    width: 300px;
  
    svg {
      stroke: #fff;
  
      // All layers are just path elements
      path {
        fill: #8A9899;
        cursor: pointer;
        outline: none;
  
        // When a layer is hovered
        &:hover {
          fill: #dac292;
        }
  
        // When a layer is focused.
        &:focus {
          fill: rgba(268,143,143,0.6);
        }
  
        // When a layer is 'checked' (via checkedLayers prop).
        &[aria-checked='true'] {
          fill: #f7cac9
        }
  
        // When a layer is 'selected' (via currentLayers prop).
        &[aria-current='true'] {
          fill: #f18973;
        }
  
        
      }
    }
  `;
    
    
    //const [date, changeDate] = React.useState(null);
    
    
    
    const onClick = ({target}) => {
      const id = target.attributes.id.value;
      const name = target.attributes.name.value;
      setRegion(id);
      callbackRegion(id);

      console.log(target)
      

    }; 
   
    return(


            
                <S id="map">
                <VectorMap {...italy}  layerProps={{onClick}}  currentLayers={[region]} />
                </S>
            

    );
};

export default Map; 
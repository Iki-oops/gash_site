import {BsFillCircleFill} from 'react-icons/bs';


const TagIcon = (props) => {
    const {color} = props;

    return (
        <BsFillCircleFill size='10px' color={color} className='tag-cicle'/>
    )
}

export default TagIcon;

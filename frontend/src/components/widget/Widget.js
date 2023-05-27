import './Widget.scss';

const Widget = ({title, children}) => {

    return (
        <div className="widget bg-box ">
            <h4 className="widget-title title medium bordered">
                <span>{title}</span>
            </h4>
            <div className='widget-info'>
                {children}
            </div>
        </div>
    )
}

export default Widget;

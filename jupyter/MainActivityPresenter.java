import com.mobotechnology.bipinpandey.mvp_hand_dirty.main_activity.model.User;

/**
 * Created by bpn on 11/30/17.
 *
 * 0. In MVP the presenter assumes the functionality of the "middle-man". All presentation logic is pushed to the presenter.
 * 1. Listens to user action and model updates
 * 2. Updates model and view
 */

public class MainActivityPresenter {
/* contain the Model(User) and View */
    private User user;
    private View view;
    /* constructor: 
    get a instance which implement the inner View interface, to create a Presenter instance:*/
    public MainActivityPresenter(View view) {
        this.user = new User();
        this.view = view;
    }
/* define series of methods about update the data of the Model instance
    these methods could be use directly;
    there,in the methods,you could operate on both the instance(of View and Model ) members ;
    this is very different the methods privided by the Model class which just opreate the Model instance data.*/
    public void updateFullName(String fullName){
        /* operate on the Model instance:user */
        user.setFullName(fullName);
        /* operate on the View instance:view */
        view.updateUserInfoTextView(user.toString());

    }
    /* similar with the updateFullName() */
    public void updateEmail(String email){
        user.setEmail(email);
        view.updateUserInfoTextView(user.toString());

    }
/* define a inner interface View(means UI Activity),which is to regular the Activity(View)'s implementation'
more important ,the specific implementation of the methods of the inner interface View will depend on the 
corresponding Activity(view); you may find that these methods don't involve the Model instance(user);
these methods may prepared for different widgets */
    public interface View{

        void updateUserInfoTextView(String info);
        void showProgressBar();
        void hideProgressBar();

    }
}
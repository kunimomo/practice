/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        unordered_set<int> result;
        ListNode* current = head;
        ListNode* previous = nullptr;

        while (current != nullptr) {
            if (result.count(current->val)) {
                previous->next = current->next;
                delete current;
                current = previous->next;
            } else {
                result.insert(current->val);
                previous = current;
                current = current->next;
            }
        }
        return head;
    }
};
